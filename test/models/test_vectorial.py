from sri.searchengine.models.vectorial import VectorModel
class TestVectorModel:
    from sri.searchengine.parser.services import CranfieldService
    # import sri.searchengine.parser.cranfield as cranfield
    # parser = CranfieldService(cranfield=cranfield)
    model = VectorModel()
    
    def test_frequency(self):
        term = 'beach'
        doc = ['hello', 'beach', 'beach', 'cousin']
        result = 2
        response = self.model.frequency(term, doc)
        assert result == response
        
    def test_max_frequency(self):
        doc = ['hello', 'beach', 'beach', 'cousin']
        result = 2
        response = self.model.max_frequency(doc)
        assert result == response
    
    def test_get_tf(self):
        term = 'beach'
        doc = ['hello', 'beach', 'beach', 'cousin']
        result = 1
        assert self.model.get_tf(term, doc) == result
        
    def test_get_tf_exception(self):
        term = 'beach'
        doc = ['hello','cousin']
        result = 0
        response = self.model.get_tf(term, doc)
        assert response == result
        
    def test_document_contains(self):
        term1 = 'beach'
        term2 = 'abeja'
        doc = ['hello', 'beach', 'beach', 'cousin']
        assert self.model.document_contains(term1, doc)
        assert not self.model.document_contains(term2, doc)
        
    def test_get_idf(self):
        from math import log10
        term = 'beach'
        doc1 = ['hello', 'beach', 'beach', 'cousin']
        doc2 = ['hello', 'amapola', 'chabel', 'cinderella']
        doc3 = ['beach', 'beach', 'cousin']
        doc4 = ['cousin']
        doc5 = ['cinderella']
        docs = [doc1, doc2, doc3, doc4, doc5]
        response = self.model.get_idf(term, docs)
        result = log10(5/2)
        assert response == result
        
    def test_get_idf_exception(self):
        from math import log10
        term = ['beach']
        doc1 = ['hello', 'amapola', 'chabel', 'cinderella']
        doc2 = ['cousin']
        doc3 = ['cinderella']
        docs = [doc1, doc2, doc3]
        response = self.model.get_idf(term, docs)
        result = 0
        assert response == result
        
    def test_get_weight(self):
        from math import log10
        term = 'beach'
        doc1 = ['hello', 'beach', 'beach', 'cousin']
        doc2 = ['hello', 'amapola', 'chabel', 'cinderella']
        doc3 = ['beach', 'beach', 'cousin']
        doc4 = ['cousin']
        doc5 = ['cinderella']
        docs = [doc1, doc2, doc3, doc4, doc5]
        response = self.model.get_weight(term, doc1, docs)
        result = 1 * log10(5/2)
        assert response == result
        
    def test_get_weight_query(self):
        from math import log10
        query = ['hello', 'beach', 'beach', 'cousin']
        term = 'hello'
        suavizado = 0.4
        doc1 = ['hello', 'beach', 'beach', 'cousin']
        doc2 = ['hello', 'amapola', 'chabel', 'cinderella']
        doc3 = ['beach', 'beach', 'cousin']
        doc4 = ['cousin']
        doc5 = ['cinderella']
        docs = [doc1, doc2, doc3, doc4, doc5]
        response = self.model.get_weight_query(term, query, suavizado, docs)
        result = 0.7 * log10(5/2)
        assert response == result
        
    def test_get_sim(self):
        doc1 = ['hello', 'beach', 'beach', 'cousin']
        doc2 = ['hello', 'amapola', 'chabel', 'cinderella']
        doc3 = ['beach', 'beach', 'cousin']
        doc4 = ['cousin']
        doc5 = ['cinderella']
        docs = [doc1, doc2, doc3, doc4, doc5]
        query = ['beach', 'bird', 'friend']
        result = 2
        response = self.model.get_sim(doc1, query, docs)
        assert result == response
        
    def test_get_ranking(self):
        query = ['beach', 'bird', 'friend']
        doc1 = ['hello beach beach cousin']
        doc2 = ['hello', 'amapola', 'chabel', 'cinderella']
        doc3 = ['beach', 'beach', 'cousin']
        doc4 = ['cousin']
        doc5 = ['cinderella']
        umbral = 0.4
        limit = 30
        docs = [doc1, doc2, doc3, doc4, doc5]
        response = self.model.get_ranking(query, docs, umbral, limit)
        result = 5
        assert response == result