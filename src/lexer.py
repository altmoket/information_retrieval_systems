import re
import stop_words

def tokenizeText(text):
    PATTERN = "[a-zA-Z]+"
    tokens = re.findall(PATTERN, text)
    return tokens

def removeStopWordsInTokens(tokens):
    ENGLISH_LANGUAGE = "english"
    stopWords = stop_words.get_stop_words(ENGLISH_LANGUAGE)
    newTokens = []
    for token in tokens:
        try:
            stopWords.index(token)
        except:
            newTokens.append(token)
    return newTokens
