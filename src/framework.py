from .document import Document
from .parser import Parser
from .exceptions import CollectionNotFound

class Framework:
    def __init__(self, collection_name, model) -> None:
        self.collection_name = collection_name
        self.model = model
        self.docs = self.get_docs()
        
    def get_docs(self):
        try:
            docs = Document.all(self.collection_name)
            docs_parsed = Parser.parse_all(docs, self.collection_name)
            return docs_parsed
        except CollectionNotFound as e:
            print(e)
            return []