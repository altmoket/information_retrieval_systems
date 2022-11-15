from src.lexer import tokenizeText, removeStopWordsInTokens

def parseCranfieldText(text):
    text = text.lower() 
    tokens = tokenizeText(text)
    terms = removeStopWordsInTokens(tokens)
    return terms
