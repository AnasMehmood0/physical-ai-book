import os
import re
from typing import List, Dict, Any
from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import Session
from ..schemas.database import DocumentDB, ChunkDB
from ..utils.text_splitter import TextSplitter
from .embedding_service import EmbeddingService

class DocumentService:
    def __init__(self, db: Session, embedding_service: EmbeddingService):
        self.db = db
        self.embedding_service = embedding_service
        self.text_splitter = TextSplitter()

    def load_docusaurus_docs(self, docs_path: str = None) -> List[Dict[str, Any]]:
        """Load all Docusaurus documentation files"""
        documents = []

        for filename in os.listdir(docs_path):
            if filename.endswith('.md'):
                file_path = os.path.join(docs_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                    # Extract title from the content (first heading or filename)
                    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                    title = title_match.group(1) if title_match else filename.replace('.md', '').replace('-', ' ').title()

                    documents.append({
                        'id': str(uuid4()),
                        'title': title,
                        'content': content,
                        'source': filename
                    })

        return documents

    def chunk_document(self, document: Dict[str, Any], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Dict[str, Any]]:
        """Split document into chunks"""
        chunks = self.text_splitter.split_text(document['content'], chunk_size, chunk_overlap)

        chunk_objects = []
        for i, chunk_text in enumerate(chunks):
            chunk_objects.append({
                'id': str(uuid4()),
                'document_id': document['id'],
                'content': chunk_text,
                'chunk_index': i
            })

        return chunk_objects

    def store_document(self, document_data: Dict[str, Any], chunks: List[Dict[str, Any]]) -> str:
        """Store document and its chunks in the database"""
        # Store document in database
        db_document = DocumentDB(
            id=document_data['id'],
            title=document_data['title'],
            content=document_data['content'],
            source=document_data['source']
        )
        self.db.add(db_document)
        self.db.commit()

        # Store chunks in database and vector store
        chunk_metadatas = []
        chunk_texts = []
        chunk_db_objects = []

        for chunk in chunks:
            # Store in database
            db_chunk = ChunkDB(
                id=chunk['id'],
                document_id=chunk['document_id'],
                content=chunk['content'],
                chunk_index=chunk['chunk_index']
            )
            self.db.add(db_chunk)
            chunk_db_objects.append(db_chunk)

            # Prepare for vector store
            chunk_texts.append(chunk['content'])
            chunk_metadatas.append({
                'document_id': chunk['document_id'],
                'chunk_id': chunk['id'],
                'source': document_data['source'],
                'title': document_data['title']
            })

        self.db.commit()

        # Store embeddings in vector store
        chunk_ids = self.embedding_service.store_embeddings(chunk_texts, chunk_metadatas)

        # Update chunk records with embedding IDs
        for i, db_chunk in enumerate(chunk_db_objects):
            db_chunk.embedding_id = chunk_ids[i]

        self.db.commit()

        return document_data['id']

    def ingest_docusaurus_docs(self, chunk_size: int = 1000, chunk_overlap: int = 200, source_path: str = None) -> Dict[str, Any]:
        """Ingest all Docusaurus documentation"""
        documents = self.load_docusaurus_docs(source_path)

        total_chunks = 0
        for doc_data in documents:
            chunks = self.chunk_document(doc_data, chunk_size, chunk_overlap)
            self.store_document(doc_data, chunks)
            total_chunks += len(chunks)

        return {
            'documents_count': len(documents),
            'chunks_count': total_chunks,
            'status': 'completed'
        }