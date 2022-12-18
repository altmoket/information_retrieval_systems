from src.lexer import tokenizeText, removeStopWordsInTokens

class Parser:
    def __init__(self, text) -> None:
        pass
    
    @staticmethod
    def parse_all(self, docs, doc_collection):
        raise NotImplementedError

class CranfieldParser(Parser):
    def __init__(self, text) -> None:
        super().__init__(text)


def parseCranfieldText(text):
    text = text.lower()
    tokens = tokenizeText(text)
    terms = removeStopWordsInTokens(tokens)
    return terms
