
from dependency_injector import containers, providers
from .services import CorpusService

from . import medline, cisi, cranfield

class ParserContainer(containers.DeclarativeContainer):
    
    cranfield_config = providers.Dependency()
    medline_config = providers.Dependency()
    cisi_config = providers.Dependency()
    tokenizer_service = providers.Dependency()
    
    cranfield_parser = providers.Singleton(
        cranfield.CranfieldParser,
        config = cranfield_config,
        tokenizer_service = tokenizer_service
    )
    
    medline_parser = providers.Singleton(
        medline.MedlineParser,
        config = medline_config,
        tokenizer_service = tokenizer_service
    )
    
    cisi_parser = providers.Singleton(
        cisi.CisiParser,
        config = cisi_config,
        tokenizer_service = tokenizer_service
    )
    
    corpus_service = providers.Singleton(
        CorpusService,
        cranfield_parser = cranfield_parser,
        medline_parser = medline_parser,
        cisi_parser = cisi_parser
    )
    