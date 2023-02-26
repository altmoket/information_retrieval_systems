from dependency_injector import containers, providers
from .parser.containers import ParserContainer
from .services import SearchEngineService
from .tokenizers.containers import TokenizerContainer
from .models.containers import RetrievalModelContainer

class SearchEngineContainer(containers.DeclarativeContainer):
    
    config = providers.Configuration()
    tokenizer_package = providers.Container(
        TokenizerContainer
    )
    
    parser_package = providers.Container(
        ParserContainer,
        cranfield_config = config.cran,
        medline_config = config.med,
        cisi_config = config.cisi,
        tokenizer_service = tokenizer_package.tokenizer_service
    )
    
    retrieval_model_package = providers.Container(
        RetrievalModelContainer,
        parser_service = parser_package.corpus_service
    )
    
    search_engine_service = providers.Singleton(
        SearchEngineService,
        retrieval_model_service = retrieval_model_package.retrieval_model_service
    )