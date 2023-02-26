from .models.services import RetrievalModelService


class SearchEngineService:
    def __init__(self, retrieval_model_service: RetrievalModelService) -> None:
        self._model = retrieval_model_service
        
    def set_model_and_corpus(self, model_name:str="VectorModel", corpus_name:str="cranfield"):
        self._model.activate_model_and_corpus(model_name, corpus_name)
    
    def get_ranking(self, query:str, collection_name:str, umbral: float, limit:int):
        ...