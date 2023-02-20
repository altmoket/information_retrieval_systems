from dependency_injector import containers, providers
from .parser.containers import ParserContainer

class SearchEngineContainer(containers.DeclarativeContainer):
    
    config = providers.Dependency()
    
    parser_package = providers.Container(
        ParserContainer,
        cranfield_config = config.cran,
        medline_config = config.med,
        cisi_config = config.cisi
    )