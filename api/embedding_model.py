from fastembed import TextEmbedding

def load_embedding_model():
    model = TextEmbedding(model_name="all-MiniLM-L6-v2")
    print("Embedding model 'all-MiniLM-L6-v2' loaded.")
    return model
