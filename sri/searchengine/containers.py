from dependency_injector import containers, providers
from .parser.containers import ParserContainer

class SearchEngineContainer(containers.DeclarativeContainer):
    
    
    parser_package = providers.Container(
        ParserContainer
    )