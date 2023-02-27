from dependency_injector import providers, containers
from .normal import NormalTokenizer
from .services import TokenizerService
from nltk.stem import WordNetLemmatizer

class TokenizerContainer(containers.DeclarativeContainer):
    
    wordnet_lemmantizer = providers.Singleton(
        WordNetLemmatizer
    )
    
    normal_tokenizer = providers.Singleton(
        NormalTokenizer,
        wordnet_lemmantizer = wordnet_lemmantizer
    )
    
    tokenizer_service = providers.Singleton(
        TokenizerService,
        normal_tokenizer = normal_tokenizer
    )