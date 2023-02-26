from . import medline, cisi, cranfield
import json

class CorpusService:
    def __init__(self, cranfield_parser:cranfield.CranfieldParser, cisi_parser: cisi.CisiParser, medline_parser: medline.MedlineParser) -> None:
        self.cranfield_parser = cranfield_parser
        self.cisi_parser = cisi_parser
        self.medline_parser = medline_parser
        self.activate_collection()
        
    def activate_collection(self, collection:str = "cranfield"):
        if collection == "cranfield":
            self._parser = self.cranfield_parser
            self.collection_name = "cranfield"
        elif collection == "medline":
            self._parser = self.medline_parser
            self.collection_name = "medline"
        elif collection == "cisi":
            self._parser = self.cisi_parser
            self.collection_name = "cisi"

    def get_documents(self):
        try:
            info = self.get_file(f'db/preprocess/{self.collection_name}_docs.json')
            return info
        except:
            txt_data = self._parser.get_txt_data()
            result = self.save_in_json(txt_data, "docs")
            return result

    def get_queries(self):
        try:
            info = self.get_file(f'db/preprocess/{self.collection_name}_qry.json')
            return info
        except:
            qry_data = self._parser.get_qry_data()
            result = self.save_in_json(qry_data, "qry")
            return result

    def get_rel(self):
        try:
            info = self.get_file(f'db/preprocess/{self.collection_name}_rel.json')
            return info
        except:
            rel = self._parser.get_rel()
            result = self.save_in_json(rel, "rel")
            return result
    
    def save_in_json(self, data, filename):
        self.create_preprocess_folder()
        with open(f'db/preprocess/{self.collection_name}_{filename}.json','w') as f:
            result = json.dump(data, f, indent=4)
            return result
            
    def get_file(self, filepath):
        with open(filepath, "r") as f:
            return f.read()
        
    def create_preprocess_folder(self):
        import os
        import errno
        try:
            os.mkdir('db/preprocess')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise