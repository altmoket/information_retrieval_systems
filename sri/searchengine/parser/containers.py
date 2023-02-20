
from dependency_injector import containers, providers
from .services import CranfieldService, CisiService, MedlineService
from . import cranfield, cisi, medline

class ParserContainer(containers.DeclarativeContainer):
    
    cisi_service = providers.Singleton(
        CisiService,
        cisi = cisi
    )
    
    cranfield_service = providers.Singleton(
        CranfieldService,
        cranfield = cranfield
    )
    
    medline_service = providers.Singleton(
        MedlineService,
        medline = medline
    )