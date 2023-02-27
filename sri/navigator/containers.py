from dependency_injector import containers, providers
from .services import NavigatorService

class NavigatorContainer(containers.DeclarativeContainer):
    
    flask_config = providers.Dependency()
    search_engine = providers.Dependency()
    
    navigator_service = providers.Singleton(
        NavigatorService,
        config = flask_config,
        search_engine = search_engine
    )
    