import os
from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name: str = None):
        """
        Initializes the embedding model.
        Args:
            model_name: The name of the sentence-transformer model to use.
                       If not provided, uses EMBEDDING_MODEL_NAME from environment.
        """
        model_name = model_name or os.getenv("EMBEDDING_MODEL_NAME", "all-MiniLM-L6-v2")
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text: str):
        """
        Generates an embedding for the given text.
        Args:
            text: The text to embed.
        Returns:
            The embedding vector.
        """
        return self.model.encode(text)
