
Doc = list[str]


class VectorModel:
    def __init__(self) -> None:
        pass

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
        pass
