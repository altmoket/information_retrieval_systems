from src import CranfieldDocument

def test_cranfield_document():
    doc = CranfieldDocument(2, "Alicia", "Alicia GOnzalez comio junto a sus amigos", "Charles", "Habana Cuba")
    result = "2\nalicia\nalicia gonzalez comio junto a sus amigos\ncharles\nhabana cuba"
    assert str(doc) == result