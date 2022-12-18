

class WrongDocCollectionNameException(Exception):
    def __str__(self) -> str:
        return "Wrong Doc Collection Name Exception"
    
class CollectionNotFound(Exception):
    def __str__(self) -> str:
        return "Collection not found"