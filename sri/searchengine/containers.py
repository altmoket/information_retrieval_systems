from dependency_injector import containers, providers
from .parser.containers import ParserContainer
from .services import SearchEngineService

class SearchEngineContainer(containers.DeclarativeContainer):
    
    config = providers.Configuration()
    
    parser_package = providers.Container(
        ParserContainer,
        cranfield_config = config.cran,
        medline_config = config.med,
        cisi_config = config.cisi
    )
    
    search_engine_service = providers.Singleton(
        SearchEngineService,
        parser_service = parser_package.corpus_service
    )