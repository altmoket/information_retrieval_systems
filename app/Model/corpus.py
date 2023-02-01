#!/usr/bin/python
#-*- coding: utf-8 -*-
from enum import Enum

class CorpusType(Enum):
    cranfield = 1
    vaswani = 2

class Corpus:
    pass

class IManager:
    pass

class CorpusManager(IManager):
    def __init__(self):
        self.colections = None
        self.parsers = None
        self.corpus_preprocessor = None

    def preprocess_corpus(self, corpus_type):
        pass
    
class CorpusPreprocessor:
    def __init__(self):
        self.corpus = None
        self.parser = None

    def preprocess(self, ):
        pass

    def set_corpus(self, ):
        pass

    def set_parser(self, ):
        pass
    

class CranfieldCorpus(Corpus):
    pass

class VaswaniCorpus(Corpus):
    pass