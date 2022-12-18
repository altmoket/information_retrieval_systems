from .document import Document
from .parser import Parser
from .exceptions import WrongDocCollectionNameException

class Framework:
    def __init__(self, doc_collection, model) -> None:
        self.doc_collection = doc_collection
        self.model = model
        self.docs = self.get_docs()
        
    def get_docs(self):
        try:
            docs = Document.all(self.doc_collection)
            docs_parsed = Parser.parse_all(docs, self.doc_collection)
            return docs_parsed
        except WrongDocCollectionNameException as e:
            print(e)
            return []