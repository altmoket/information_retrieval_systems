from .parser.services import CorpusService


class SearchEngineService:
    def __init__(self, parser_service: CorpusService) -> None:
        self._parser = parser_service
        
    def get_documents(self, collection: str = "cranfield"):
        self._parser.activate_collection(collection)
        docs = self._parser.get_documents()
        return docs
    
    def get_queries(self, collection: str = "cranfield"):
        self._parser.activate_collection(collection)
        queries = self._parser.get_queries()
        return queries
    
    def get_rel(self, collection: str = "cranfield"):
        self._parser.activate_collection(collection)
        rel = self._parser.get_rel()
        return rel