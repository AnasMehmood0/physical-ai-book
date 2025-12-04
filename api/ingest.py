import os
import argparse
from qdrant_client.http.models import PointStruct
from qdrant_client import QdrantClient
from fastembed import TextEmbedding
from langchain_text_splitters import RecursiveCharacterTextSplitter
from api.vector_store import initialize_qdrant_client
from api.embedding_model import load_embedding_model


def read_markdown_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def recursive_character_chunking(text: str) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_text(text)


def upsert_chunks_to_qdrant(client: QdrantClient, embedding_model: TextEmbedding, chunks: list[str], chapter_id: str):
    if not chunks:
        return

    # Generate embeddings for the chunks
    embeddings = embedding_model.embed_documents(chunks)

    points = [
        PointStruct(
            id=idx,
            vector=embedding.tolist(),  # Convert numpy array to list
            payload={
                "chapter_id": chapter_id,
                "chunk_content": chunk
            },
        )
        for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings))
    ]

    client.upsert(collection_name="physical_ai_book", points=points, wait=True)
    print(f"Upserted {len(chunks)} chunks to Qdrant for chapter_id: {chapter_id}")


def ingest_chapter(chapter_file_path: str, client: QdrantClient, embedding_model: TextEmbedding):
    print(f"Ingesting {chapter_file_path}...")
    content = read_markdown_file(chapter_file_path)
    chunks = recursive_character_chunking(content)
    chapter_id = os.path.splitext(os.path.basename(chapter_file_path))[0]  # e.g., "chapter1"
    upsert_chunks_to_qdrant(client, embedding_model, chunks, chapter_id)
    print(f"Finished ingesting {chapter_file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest markdown files into Qdrant.")
    parser.add_argument(
        "--path",
        type=str,
        default="../web/docs",
        help="Path to the directory containing markdown chapter files.",
    )
    args = parser.parse_args()

    qdrant_client = initialize_qdrant_client()
    embedding_model = load_embedding_model()

    docs_path = args.path
    for root, _, files in os.walk(docs_path):
        for file in files:
            if file.endswith(".md"):
                ingest_chapter(os.path.join(root, file), qdrant_client, embedding_model)
