
import re

class DataCleaner:

    @staticmethod
    def clean_text( text:str)-> str:
        """
        Clean text for use in a RAG system.

        Args:
            text (str): The raw text to be cleaned.

        Returns:
            str: The cleaned text.
        """

        # Remove HTML tags
        text = re.sub(r"<[^>]*>", "", text)

        # Normalize whitespace
        text = re.sub(r"\s+", " ", text).strip()

        # Remove punctuation (except apostrophes)
        text = re.sub(r"[^\w\s']", "", text)

        # Lowercase the text
        text = text.lower()
    
        return text