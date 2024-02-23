import enum

from langchain_openai import OpenAIEmbeddings

class EmbeddingType(enum.Enum):
    """
    Enum representing supported embedding types.

    - OPENAI: OpenAI API text embeddings.
    # Add four additional embedding types based on your research and requirements:
    # - UNIVERSAL_SENTENCE_ENCODER: TensorFlow Universal Sentence Encoder embeddings.
    # - LAUDA: LAUDA multilingual embeddings.
    # - FLAIR: FLAIR text embeddings with various pre-trained models.
    # - SentenceTransformers: SentenceTransformers with support for multiple pre-trained models.

    OPENAI = "openai"
    # ... Other embedding types as defined above ...

    """

    OPENAI = "openai"
    UNIVERSAL_SENTENCE_ENCODER = "universal_sentence_encoder"
    LAUDA = "lauda"
    FLAIR = "flair"
    SENTENCE_TRANSFORMERS= "sentence_transformers"

class EmbeddingFactory:
    """
    Provides a factory for creating embedding objects based on specified types and optional default models.

    This factory maintains a mapping of supported embedding types to their corresponding implementation classes and
    allows specifying default models for each type. It can be used to easily create embedding objects with optional
    model customization.
    """

    def __init__(self):
        """
        Initializes the factory with available embedding types, their implementation classes, and default models.
        """
        self.embedding_classes = {
            EmbeddingType.OPENAI: (OpenAIEmbeddings, "text-davinci-003"),  # (class, default model)
            # Add mappings for other embedding types, classes, and default models here
            # Example:
            # EmbeddingType.UNIVERSAL_SENTENCE_ENCODER: (USESentenceEncoder, "tf-universal-sentence-encoder-multilingual"),
            # EmbeddingType.LAUDA: (LaudaEmbeddings, "laus-base"),
            # EmbeddingType.FLAIR: (FlairTextEmbeddings, "en-wiki-base-v2"),
            # EmbeddingType.SentenceTransformers: (SentenceTransformersEmbeddings, "all-mpnet-base-v2"),
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
        return embedding_class(model=model or default_model)

    def list_supported_embeddings(self) -> list[EmbeddingType]:
        """
        Returns a list of supported embedding types.

        Returns:
            list[EmbeddingType]: The list of supported embedding types.
        """

        return list(self.embedding_classes.keys())

# Example usage:
embedding_factory = EmbeddingFactory()

# Create an OpenAI embedding using default model
openai_embedding = embedding_factory.create_embedding(EmbeddingType.OPENAI)

# Create an OpenAI embedding using a specific model
specific_openai_embedding = embedding_factory.create_embedding(EmbeddingType.OPENAI, model="text-curie-001")

# Create other embeddings with default or specified models (replace with actual classes)
# use_embedding = embedding_factory.create_embedding(EmbeddingType.UNIVERSAL_SENTENCE_ENCODER, model="distilbert-base-uncased-multilingual-cased")
# lauda_embedding = embedding_factory.create_embedding(EmbeddingType.LAUDA)
# flair_embedding = embedding_factory.create_embedding(EmbeddingType.FLAIR, model="de-wiki-base-v2")
# sentence_transformers_embedding = embedding_factory.create_embedding(EmbeddingType.SentenceTransformers, model="paraphrase-multilingual-mpnet-base-v2")

# Use the created
