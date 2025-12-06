from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initializes the embedding model.
        Args:
            model_name: The name of the sentence-transformer model to use.
        """
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
