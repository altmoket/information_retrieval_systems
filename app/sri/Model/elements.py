#!/usr/bin/python
#-*- coding: utf-8 -*-


class Query():
    def __init__(self):
        self.tokens = None

class BooleanQuery(Query):
    pass

class Document:
    def __init__(self):
        self.tokens = None