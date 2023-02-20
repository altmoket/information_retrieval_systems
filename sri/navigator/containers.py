from dependency_injector import containers, providers
from .services import FlaskService

class FlaskContainer(containers.DeclarativeContainer):
    
    config = providers.Dependency()
    search_engine = providers.Dependency()
    
    flask_service = providers.Singleton(
        FlaskService,
        config = config,
        search_engine = search_engine
    )
    