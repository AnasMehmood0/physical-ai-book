import os
import argparse
from langchain_text_splitters import RecursiveCharacterTextSplitter
from api.vector_store import VectorStore

def ingest_documents(directory_path: str, vector_store: VectorStore):
    """
    Ingests all text documents from a directory into the vector store.
    Args:
        directory_path: The path to the directory containing the documents.
        vector_store: An instance of the VectorStore.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith((".txt", ".md")):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                chunks = text_splitter.split_text(content)
                
                # Assuming chapter_id is derived from the file name or path
                # This needs to be adapted to the actual book structure
                chapter_id = os.path.splitext(file)[0]
                metadatas = [{"chapter_id": chapter_id, "source": file} for _ in chunks]
                
                vector_store.add_documents(chunks, metadatas)
                print(f"Ingested {len(chunks)} chunks from {file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest book content into the vector database.")
    parser.add_argument("directory", type=str, help="The directory containing the book content (.txt files).")
    args = parser.parse_args()

    vs = VectorStore()
    ingest_documents(args.directory, vs)
    print("Ingestion complete.")
