import os
import google.generativeai as genai

class EmbeddingModel:
    def __init__(self, model_name: str = None):
        """
        Initializes the embedding model using Google Gemini.
        Args:
            model_name: The name of the embedding model to use.
                       If not provided, uses 'models/text-embedding-004'.
        """
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")

        genai.configure(api_key=api_key)
        self.model_name = model_name or "models/text-embedding-004"
        self.dimension = 768  # Gemini text-embedding-004 dimension

    def get_embedding(self, text: str):
        """
        Generates an embedding for the given text using Gemini.
        Args:
            text: The text to embed.
        Returns:
            The embedding vector as a list.
        """
        result = genai.embed_content(
            model=self.model_name,
            content=text,
            task_type="retrieval_document"
        )
        return result['embedding']

    def get_sentence_embedding_dimension(self):
        """
        Returns the dimension of the embedding vectors.
        """
        return self.dimension
