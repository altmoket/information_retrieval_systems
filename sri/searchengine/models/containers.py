from dependency_injector import providers, containers
from .vectorial import VectorModel
from .services import RetrievalModelService


class RetrievalModelContainer(containers.DeclarativeContainer):
    parser_service = providers.Dependency()

    vector_model = providers.Singleton(
        VectorModel,
        parser_service = parser_service
    )
    
    retrieval_model_service = providers.Singleton(
        RetrievalModelService,
        vector_model = vector_model
    )