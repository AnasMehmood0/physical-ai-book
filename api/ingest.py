import os
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
            if file.endswith(".txt"): # Assuming .txt files for now
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
    # This is an example of how to run the ingestion.
    # The actual directory should be provided.
    # For now, we will create a dummy directory and file for testing.
    vs = VectorStore()
    
    # Create dummy data for demonstration
    if not os.path.exists("temp_book"):
        os.makedirs("temp_book")
    with open("temp_book/chapter1.txt", "w") as f:
        f.write("This is the first chapter of the book about AI.\n" * 20)
    with open("temp_book/chapter2.txt", "w") as f:
        f.write("This is the second chapter, focusing on LLMs.\n" * 20)

    ingest_documents("temp_book", vs)
