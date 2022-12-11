import ir_datasets
from ir_datasets.util import math
from src.parser import parseCranfieldText
from src.utils import matchText, booleanToInt, existItemInList

def rankingOfDocumentsGivenQueryDocsAndUmbral(query, docs, umbral = 0.6):
    listOfDocumentsRetrieve = listOfRetrieveDocumentsGivenQueryDocs(query, docs)
    ranking = []
    for (doc,similitud) in listOfDocumentsRetrieve:
        if similitud > umbral:
            ranking.append((doc, similitud))
    return ranking # Falta ordenarlos

def listOfRetrieveDocumentsGivenQueryDocs(query, docs):
    idfCollection = idfCollectionGivenQueryAndDocs(query, docs)
    listOfRetrieveDocuments = []
    for doc in docs:
        similitud = simQueryDoc(query, doc, idfCollection)
        listOfRetrieveDocuments.append((doc, similitud))
    return listOfRetrieveDocuments

def idfCollectionGivenQueryAndDocs(query, docs):
    idfCollection = []
    for term in query:
        idf_term_in_docs = idfTermInDocs(term, docs)
        idfCollection.append(idf_term_in_docs)
    return idfCollection

def simQueryDoc(query, doc, idfCollection, suavizado = 0.4):
    sum_prod_weight = 0
    sum_square_weight_query = 0
    sum_square_weight_doc = 0
    for idf,term in zip(idfCollection,query):
        weight_term_doc = weightTermDoc(term, doc, idf)
        weight_term_query = weightTermQuery(term, query, idf, suavizado)
        sum_prod_weight += weight_term_doc * weight_term_query
        sum_square_weight_doc += weight_term_doc ** 2
        sum_square_weight_query += weight_term_query ** 2
    sqrt_sum_square_weight_query = math.sqrt(sum_square_weight_query)
    sqrt_sum_square_weight_doc = math.sqrt(sum_square_weight_doc)
    return sim(sum_prod_weight, sqrt_sum_square_weight_query, sqrt_sum_square_weight_doc)

def idfTermInDocs(term, docs):
    numberOfDocuments = len(docs)
    documentsThatContainsTerm = numberOfDocumentsWhichContainsTerm(docs, term)
    return idf(numberOfDocuments, documentsThatContainsTerm)

def weightTermDoc(term, doc, idf): # Lo mismo para el siguiente metodo
    tf_term_doc = tfTermInStringCollection(term, doc)
    return tf_term_doc * idf

def weightTermQuery(term, query, idf, suavizado = 0.4): # el weight solo depende del tf e idf. Arreglar
    tf_term_query = tfTermInStringCollection(term, query)
    weight = (suavizado + (1 - suavizado) * tf_term_query) * idf
    return weight

def tfTermInStringCollection(term, collection):
    frequency = frequencyTermInDoc(term, collection)
    maxFrequency = maxFrequencyInDoc(collection)
    return tf(frequency, maxFrequency)

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

def numberOfDocumentsWhichContainsTerm(docs, term):
    numberOfDocuments = 0
    for doc in docs:
        increment = booleanToInt(existItemInList(term, doc)) 
        numberOfDocuments += increment
    return numberOfDocuments

def sim(sum_prod_weight, sqrt_sum_square_weight_query, sqrt_sum_square_weight_doc):
    try:
        return sum_prod_weight / (sqrt_sum_square_weight_query * sqrt_sum_square_weight_doc)
    except:
        return 0

def idf(numberOfDocuments, documentsThatContainsTerm):
    try:
        idf = math.log(numberOfDocuments/documentsThatContainsTerm)
        return idf
    except:
        return 0

def tf(frequency, maxFrequency):
    try:
        return frequency/maxFrequency
    except:
        return 0



def rankingOfUserQuery(query, umbral=0.4):
    dataSet = cranfieldDataset() 
    docs = parsedCranfieldDocuments(dataSet)
    ranking = rankingOfDocumentsGivenQueryDocsAndUmbral(query, docs, umbral)
    return ranking

def cranfieldDataset():
    CORPUS = "cranfield"
    return ir_datasets.load(CORPUS)

def parsedCranfieldDocuments(dataSet):
    docs = []
    for doc in dataSet.docs_iter():
        docTerms = parseCranfieldText(doc.text)
        docs.append(docTerms)
    return docs
