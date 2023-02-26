from .vectorial import VectorModel


class RetrievalModelService:
    def __init__(self, vector_model: VectorModel) -> None:
        self._vector = vector_model
        
    def activate_model_and_corpus(self, model_name:str="VectorModel", corpus_name:str = "cranfield"):
        if model_name == "VectorModel":
            self._model = self._vector
        elif model_name == "BooleanModel":
            ... 
        self._model.activate_corpus(corpus_name)
            
    def get_ranking(self, query:str, umbral:float, limit:int):
       ... 
        # ranking = self._model.get_ranking(query, umbral, limit)
        # return ranking