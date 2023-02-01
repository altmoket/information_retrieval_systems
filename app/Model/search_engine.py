#!/usr/bin/python
#-*- coding: utf-8 -*-
from .corpus import CorpusType, CorpusManager
from .models import Model

class SearchEngine:
    def __init__(self, corpus_manager, models):
        self.corpus_manager = corpus_manager
        self.models = models

    def get_documents(self, corpus_type:CorpusType):
        pass

    def get_queries(self, corpus_type:CorpusType):
        pass

    def run_query(self, query:str, corpus_type:CorpusType, model:Model):
        pass

    def preprocess_all_corpus(self):
        pass

