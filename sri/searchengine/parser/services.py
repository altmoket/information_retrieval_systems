from . import medline, cisi, cranfield

class CorpusService:
    def __init__(self, cranfield_parser:cranfield.CranfieldParser, cisi_parser: cisi.CisiParser, medline_parser: medline.MedlineParser) -> None:
        self.cranfield_parser = cranfield_parser
        self.cisi_parser = cisi_parser
        self.medline_parser = medline_parser
        self.activate_collection()
        
    def activate_collection(self, collection:str = "cranfield"):
        if collection == "cranfield":
            self._parser = self.cranfield_parser
        elif collection == "medline":
            self._parser = self.medline_parser
        elif collection == "cisi":
            self._parser = self.cisi_parser

    def get_documents(self):
        txt_data = self._parser.get_txt_data()
        return txt_data

    def get_queries(self):
        qry_data = self._parser.get_qry_data()
        return qry_data

    def get_rel(self):
        rel = self._parser.get_rel_numpy()
        return rel