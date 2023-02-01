#!/usr/bin/python
#-*- coding: utf-8 -*-

class IParser:
    pass

class ICorpusParser(IParser):
    def __init__(self):
        self.corpus_type = None

    def parse(self, corpus):
        pass
    
class CranfieldParser(ICorpusParser):
    pass

class VaswaniParser(ICorpusParser):
    pass

class SimpleParser(IParser):
    def __init__(self):
        pass

    def parse(self, text):
        pass
    
class BooleanParser(SimpleParser):
    pass

