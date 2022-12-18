from .configuration import Configuration, File
from.exceptions import CollectionNotFound

class Document:
    def __init__(self, id, text) -> None:
        self.id = id
        self.text = text.lower()
        
    @staticmethod
    def all(collection_name):
        try:
            docs_path = Configuration().get(collection_name, 'docs')
            docs = File(docs_path).open()
            return docs
        except:
            raise CollectionNotFound()

class CranfieldDocument(Document):
    def __init__(self, id, title, text, author, editorial) -> None:
        super().__init__(id, text)
        self.title = title.lower()
        self.author = author.lower()
        self.editorial = editorial.lower()
        
    def __str__(self) -> str:
        result = f"{self.id}\n"
        result+= f"{self.title}\n"
        result+= f"{self.text}\n"
        result+= f"{self.author}\n"
        result+= f"{self.editorial}"
        return result