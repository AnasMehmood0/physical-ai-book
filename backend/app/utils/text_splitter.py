import re
from typing import List

class TextSplitter:
    def __init__(self):
        pass

    def split_text(self, text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
        """
        Split text into chunks of specified size with overlap
        """
        if len(text) <= chunk_size:
            return [text]

        chunks = []
        start = 0

        while start < len(text):
            # Determine the end position
            end = start + chunk_size

            # If we're at the end, take the remaining text
            if end >= len(text):
                chunks.append(text[start:])
                break

            # Try to break at sentence boundary
            chunk = text[start:end]

            # Find the last sentence ending within the chunk
            sentence_end = max(
                chunk.rfind('.'),
                chunk.rfind('!'),
                chunk.rfind('?'),
                chunk.rfind('\n'),
                chunk.rfind(';'),
                chunk.rfind(',')
            )

            # If we found a good break point and it's not too close to the start
            if sentence_end > chunk_size // 2:
                end = start + sentence_end + 1
                chunk = text[start:end]

            chunks.append(chunk)

            # Move start position with overlap
            start = end - chunk_overlap if chunk_overlap < end else end

            # If overlap would cause us to go backwards, move to next full chunk
            if start <= 0:
                start = end

        # Clean up any chunks that are too short (unless it's the only one)
        cleaned_chunks = []
        for chunk in chunks:
            if len(chunk.strip()) > 10:  # Only keep chunks with substantial content
                cleaned_chunks.append(chunk)

        return cleaned_chunks