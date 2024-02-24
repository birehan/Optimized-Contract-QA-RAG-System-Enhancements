import enum
from langchain_community.embeddings import SentenceTransformerEmbeddings, OpenAIEmbeddings



from dotenv import load_dotenv,find_dotenv

class EmbeddingType(enum.Enum):
    OPENAI_EMBEDDING = "OpenAI Embedding"
    SENTENCE_TRANSFORMER_EMBEDDING = "Sentence Transformers"

class EmbeddingFactory:
    """
    Provides a factory for creating embedding objects based on specified types and optional default models.

    This factory maintains a mapping of supported embedding types to their corresponding implementation classes and
    allows specifying default models for each type. It can be used to easily create embedding objects with optional
    model customization.
    """

    def __init__(self):
        load_dotenv(find_dotenv())


        """
        Initializes the factory with available embedding types, their implementation classes, and default models.
        """
        self.embedding_classes = {
            EmbeddingType.SENTENCE_TRANSFORMER_EMBEDDING: (SentenceTransformerEmbeddings, "all-MiniLM-L6-v2"),  
            EmbeddingType.OPENAI_EMBEDDING: (OpenAIEmbeddings, "text-embedding-ada-002"),  
        }

    def create_embedding(self, embedding_type: EmbeddingType, model: str = None) -> object:
        """
        Creates an embedding object of the specified type and optionally uses the provided model.

        Args:
            embedding_type (EmbeddingType): The type of embedding to create.
            model (str, optional): The specific model to use. Defaults to the type's default model.

        Returns:
            object: The created embedding object.

        Raises:
            ValueError: If the specified embedding type is not supported.
        """

        if embedding_type not in self.embedding_classes:
            raise ValueError(f"Unsupported embedding type: {embedding_type}")

        embedding_class, default_model = self.embedding_classes[embedding_type]
        print(embedding_class, default_model)
        if embedding_type == EmbeddingType.OPENAI_EMBEDDING:
            return embedding_class(model=model or default_model)
        else:
            return embedding_class(model_name=model or default_model)

    @staticmethod
    def list_supported_embeddings():
        """
        """

        return {
            "items": [{"key": enum_type.name, "value":enum_type.value } for enum_type in EmbeddingType],
            "name": "embedding",
            "label": "Embedding Models"
        }

