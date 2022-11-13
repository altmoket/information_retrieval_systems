import re
import ir_datasets
from ir_datasets.util import math
import stop_words
# print(dataSet.docs_count())
# print(dataSet.queries_count())
#
#
# def getDocumentIteratorFromDataset(dataSet):
#     return dataSet.docs_iter()

# for query in dataSet.queries_iter():
#     print(query.text)


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

def frequencyTermInDoc(term, doc):
    frequency = 0
    INCREMENT = 1
    for word in doc:
        if term == word:
            frequency += INCREMENT
    return frequency

def maxFrequencyInDoc(doc):
    maxFrequency = 0
    for term in doc:
        frequency = frequencyTermInDoc(term, doc)
        if frequency > maxFrequency:
            maxFrequency = frequency
    return maxFrequency

def tfTermInDoc(term, doc):
    frequency = frequencyTermInDoc(term, doc)
    maxFrequency = maxFrequencyInDoc(doc)
    return frequency/maxFrequency

def existTermInDoc(term, doc):
    EXIST = True
    for word in doc:
        if word == term:
            return EXIST
    return not EXIST

def numberOfDocumentsWhichContainsTerm(docs, term):
    numberOfDocuments = 0
    INCREMENT = 1
    for doc in docs:
        existTerm = existTermInDoc(term, doc)
        if existTerm:
            numberOfDocuments += INCREMENT
    return numberOfDocuments

def idfTermInDocs(term, docs):
    numberOfDocuments = len(docs)
    documentsThatContainsTerm = numberOfDocumentsWhichContainsTerm(docs, term)
    idf = math.log(numberOfDocuments/documentsThatContainsTerm)
    return idf

def weightsDictOfTermsInDocuments(terms, docs):
    weights = dict()
    for term in terms:
        idf = idfTermInDocs(term, docs)
        for doc in docs:
            tf = tfTermInDoc(term, doc)
            weights[term] = tf * idf
    return weights

def main():
    CORPUS = "cranfield"
    dataSet = ir_datasets.load(CORPUS)
    terms = []
    for query in dataSet.queries_iter():
        tokens = tokenizeText(query.text)
        terms = removeStopWordsInTokens(tokens)
        print(terms)

MAIN = "__main__"
if __name__ == MAIN:
    try:
        main()
    except Exception as e:
        print(e)
