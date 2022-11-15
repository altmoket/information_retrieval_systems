import ir_datasets
from ir_datasets.util import math
from src.parser import parseCranfieldText
from src.utils import matchText, booleanToInt
# print(dataSet.docs_count())
# print(dataSet.queries_count())
#
#
# def getDocumentIteratorFromDataset(dataSet):
#     return dataSet.docs_iter()

# for query in dataSet.queries_iter():
#     print(query.text)

def frequencyTermInDoc(term, doc):
    frequency = 0
    for docTerm in doc:
        increment = booleanToInt(matchText(term, docTerm))
        frequency += increment
    return frequency

def maxFrequencyInDoc(doc):
    maxFrequency = 0
    for term in doc:
        frequency = frequencyTermInDoc(term, doc)
        if frequency > maxFrequency:
            maxFrequency = frequency
    return maxFrequency

def tfTermInStringCollection(term, collection):
    frequency = frequencyTermInDoc(term, collection)
    maxFrequency = maxFrequencyInDoc(collection)
    return tf(frequency, maxFrequency)

def tf(frequency, maxFrequency):
    try:
        return frequency/maxFrequency
    except:
        return 0

def existTermInDoc(term, doc):
    EXIST = True
    for docTerm in doc:
        if matchText(docTerm, term):
            return EXIST
    return not EXIST

def numberOfDocumentsWhichContainsTerm(docs, term):
    numberOfDocuments = 0
    for doc in docs:
        increment = booleanToInt(existTermInDoc(term, doc)) 
        numberOfDocuments += increment
    return numberOfDocuments



def idfTermInDocs(term, docs):
    numberOfDocuments = len(docs)
    documentsThatContainsTerm = numberOfDocumentsWhichContainsTerm(docs, term)
    return idf(numberOfDocuments, documentsThatContainsTerm)

def idf(numberOfDocuments, documentsThatContainsTerm):
    try:
        idf = math.log(numberOfDocuments/documentsThatContainsTerm)
        return idf
    except:
        return 0

def weightsDictOfTermsInDocuments(terms, docs):
    lenTerms = len(terms)
    lenDocs = len(docs)
    weights = [[]] * lenTerms
    for i,term in zip(range(lenTerms),terms):
        idf = idfTermInDocs(term, docs)
        for j,doc in zip(range(lenDocs), docs):
            tf = tfTermInStringCollection(term, doc)
            print(tf)
            weights[i].append(tf * idf)
    return weights



def weightTermDoc(term, doc, idf):
    tf_term_doc = tfTermInStringCollection(term, doc)
    return tf_term_doc * idf

def weightTermQuery(term, query, idf, suavizado = 0.4):
    tf_term_query = tfTermInStringCollection(term, query)
    weight = (suavizado + (1 - suavizado) * tf_term_query) * idf
    return weight

def simDocQuery(doc, query, idf, suavizado = 0.4):
    sum_prod_weight = 0
    sum_square_weight_query = 0
    sum_square_weight_doc = 0
    for term in query:
        weight_term_doc = weightTermDoc(term, doc, idf)
        weight_term_query = weightTermQuery(term, query, idf, suavizado)
        sum_prod_weight += weight_term_doc * weight_term_query
        sum_square_weight_doc += weight_term_doc ** 2
        sum_square_weight_query += weight_term_query ** 2
    sqrt_sum_square_weight_query = math.sqrt(sum_square_weight_query)
    sqrt_sum_square_weight_doc = math.sqrt(sum_square_weight_doc)
    return sum_prod_weight / (sqrt_sum_square_weight_query * sqrt_sum_square_weight_doc) 

def rankingOfDocumentsGivenQueryAndDocs(query, docs):
    pass
     
        


# print(f"{doc.doc_id=}")
# print(f"{doc.author=}")
# print(f"{doc.title=}")
# print(f"{doc.text=}")
# print(f"{doc.bib=}")
import sys
def consoleApp():
    pass

def main():
    CORPUS = "cranfield"
    dataSet = ir_datasets.load(CORPUS)
    queriesInTokens = []
    for query in dataSet.queries_iter():
        queryTerms = parseCranfieldText(query.text)
        queriesInTokens.append(queryTerms)
        break
    docsInTokens = []
    for doc in dataSet.docs_iter():
        docTerms = parseCranfieldText(doc.text)
        docsInTokens.append(docTerms)
    # weights = weightsDictOfTermsInDocuments(queriesInTokens[0], docsInTokens)
    # print(weights)
    queryWeights = weightsDictOfTermsInDocuments(queriesInTokens[0], queriesInTokens[0])
    print(queryWeights)

MAIN = "__main__"
if __name__ == MAIN:
    try:
        main()
    except Exception as e:
        print(e)
