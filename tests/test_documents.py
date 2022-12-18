from src import CranfieldDocument, Document
from src.exceptions import CollectionNotFound

def test_cranfield_document():
    doc = CranfieldDocument(2, "Alicia", "Alicia GOnzalez comio junto a sus amigos", "Charles", "Habana Cuba")
    result = "2\nalicia\nalicia gonzalez comio junto a sus amigos\ncharles\nhabana cuba"
    assert str(doc) == result
    
def test_all():
    docs = Document.all('cranfield')
    print(docs)
    assert docs is not None
    
def test_notFoundCollection():
    try:
        docs = Document.all('aaaaa')
    except Exception as e:
        assert isinstance(e, CollectionNotFound)
        
    
    