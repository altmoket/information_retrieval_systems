from . import cranfield, cisi, medline

class CorpusService:
    def __init__(self, parser) -> None:
        self._parser = parser
    
    def get_documents(self, PATH_TO_FILE):
        data = self.get_data(PATH_TO_FILE)
        txt_data = self.get_txt_data(txt_list=data)
        return txt_data
    
    def get_queries(self, PATH_TO_FILE):
        data = self.get_data(PATH_TO_FILE)
        txt_data = self.get_qry_data(qry_list=data)
        return txt_data
    
    def get_rel(self, PATH_TO_REL):
        rel = self.get_rel_numpy(PATH_TO_REL)
        return rel
    
    def _get_data(self, PATH_TO_FILE):
        return self._parser.get_data(PATH_TO_FILE=PATH_TO_FILE)
    
    
    def _get_txt_data(self, txt_list: list[str]):
        return self._parser.get_txt_data(txt_list)
    
    
    def _get_qry_data(self, qry_list: list[str]):
        return self._parser.get_qry_data(qry_list)
    
    
    def _get_rel(self, PATH_TO_REL: str):
        return self._parser.get_rel(PATH_TO_REL)
    
    
    def _get_rel_numpy(self, PATH_TO_REL: str):
        return self._parser.get_rel_numpy(PATH_TO_REL)

class CranfieldService(CorpusService):
    def __init__(self, cranfield: cranfield) -> None:
        super().__init__(cranfield)

class MedlineService(CorpusService):
    def __init__(self, medline: medline) -> None:
        super().__init__(medline)

class CisiService(CorpusService):
    def __init__(self, cisi: cisi) -> None:
        super().__init__(cisi)