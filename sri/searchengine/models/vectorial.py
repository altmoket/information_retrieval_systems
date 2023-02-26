import json
from ..parser.services import CorpusService
Doc = list[str]


class VectorModel:
    def __init__(self, parser_service: CorpusService) -> None:
        self._parser = parser_service
        
    def activate_corpus(self, corpus_name: str = "cranfield"):
        self._parser.activate_corpus(corpus_name)
        info:dict = json.loads(self._parser.get_documents())
        self.docs = [value["tokens"] for _, value in info.items()]

    def frequency(self, term: str, doc: Doc) -> int:
        return doc.count(term)

    def max_frequency(self, doc: Doc) -> int:
        max_frequency = 0
        for term in doc:
            count = doc.count(term)
            max_frequency = count if count > max_frequency else max_frequency
        return max_frequency

    def get_tf(self, term: str, doc: Doc) -> float:
        frequency = self.frequency(term, doc)
        max_frequency = self.max_frequency(doc)
        return frequency / max_frequency

    def document_contains(self, term: str, doc: Doc) -> bool:
        try:
            doc.index(term)
            return True
        except:
            return False

    def get_idf(self, term: str, docs: list[Doc]) -> float:
        from math import log10
        num_docs = len(docs)
        num_docs_contains_term = sum(
            [1 for doc in docs if self.document_contains(term, doc)])
        try:
            return log10(num_docs/num_docs_contains_term)
        except:
            return 0

    def get_weight(self, term: str, doc: list[str], docs: list[Doc]) -> float:
        tf = self.get_tf(term, doc)
        idf = self.get_idf(term, docs)
        return tf * idf

    def get_weight_query(self, term: str, query: list[str], suavizado: float, docs: list[Doc]) -> float:
        tf = self.get_tf(term, query)
        idf = self.get_idf(term, docs)
        result = (suavizado + (1-suavizado) * tf) * idf
        return result
    
    def get_sim(self, doc:Doc, query:list[str], docs:list[Doc]):
        for term in query:
            weight_term_doc = self.get_weight(term, doc, docs)
            weight_term_query = self.get_weight_query()
            

    def save_in_json(self, data, filename):
        with open(f'db/preprocess/vector_{self.corpus_name}_{filename}.json','w') as f:
            result = json.dump(data, f, indent=4)
            return result
            
    def get_file(self, filepath):
        with open(filepath, "r") as f:
            return f.read()
