from dependency_injector import containers, providers
from .searchengine.containers import SearchEngineContainer
from .navigator.containers import FlaskContainer


class SriContainer(containers.DeclarativeContainer):
    
    config = providers.Configuration()
    
    search_engine_package = providers.Container(
        SearchEngineContainer,
        config = config
    )
    
    flask_package = providers.Container(
        FlaskContainer,
        config = config.flask,
        search_engine = search_engine_package.search_engine_service
    )
    
    