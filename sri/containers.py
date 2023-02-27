from dependency_injector import containers, providers
from .searchengine.containers import SearchEngineContainer
from .navigator.containers import NavigatorContainer


class SriContainer(containers.DeclarativeContainer):
    
    config = providers.Configuration()
    
    search_engine_package = providers.Container(
        SearchEngineContainer,
        config = config
    )
    
    navigator_package = providers.Container(
        NavigatorContainer,
        flask_config = config.flask,
        search_engine = search_engine_package.search_engine_service
    )
    
    