from dependency_injector import providers, containers
from .normal import NormalTokenizer
from .services import TokenizerService

class TokenizerContainer(containers.DeclarativeContainer):
    
    normal_tokenizer = providers.Singleton(
        NormalTokenizer
    )
    
    tokenizer_service = providers.Singleton(
        TokenizerService,
        normal_tokenizer = normal_tokenizer
    )