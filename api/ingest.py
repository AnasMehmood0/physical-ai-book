import os
import argparse
from dotenv import load_dotenv
from langchain_text_splitters import MarkdownTextSplitter
from vector_store import VectorStore

# Load environment variables
load_dotenv()

def ingest_documents(directory_path: str, vector_store: VectorStore):
    """
    Ingests all text documents from a directory into the vector store.
    Args:
        directory_path: The path to the directory containing the documents.
        vector_store: An instance of the VectorStore.
    """
    # Get chunk configuration from environment
    chunk_size = int(os.getenv("CHUNK_SIZE", "256"))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "32"))

    text_splitter = MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

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

                # Create metadatas with the actual text content included
                metadatas = [
                    {
                        "chapter_id": chapter_id,
                        "source": file,
                        "text": chunk  # Store the actual text content
                    }
                    for chunk in chunks
                ]

                vector_store.add_documents(chunks, metadatas)
                print(f"Ingested {len(chunks)} chunks from {file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest book content into the vector database.")
    parser.add_argument("directory", type=str, help="The directory containing the book content (.txt files).")
    args = parser.parse_args()

    vs = VectorStore()
    ingest_documents(args.directory, vs)
    print("Ingestion complete.")
