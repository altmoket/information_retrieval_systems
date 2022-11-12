import re
import ir_datasets
import stop_words
# print(dataSet.docs_count())
# print(dataSet.queries_count())
#
#
# def getDocumentIteratorFromDataset(dataSet):
#     return dataSet.docs_iter()

# for query in dataSet.queries_iter():
#     print(query.text)


def tokenizeQuery(query):
    return query.split()

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

def main():
    CORPUS = "cranfield"
    dataSet = ir_datasets.load(CORPUS)
    for query in dataSet.queries_iter():
        tokens = tokenizeQuery(query.text)
        tokens = removeStopWordsInTokens(tokens)
        print(tokens)

MAIN = "__main__"
if __name__ == MAIN:
    try:
        main()
    except Exception as e:
        print(e)
