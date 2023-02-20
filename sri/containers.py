from dependency_injector import containers, providers
from .searchengine.containers import SearchEngineContainer


class SriContainer(containers.DeclarativeContainer):
    
    config = providers.Configuration()
    
    search_engine_package = providers.Singleton(
        SearchEngineContainer
    )
    
    