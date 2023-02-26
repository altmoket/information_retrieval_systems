from ..tokenizers.services import TokenizerService


class CorpusParser:
    def __init__(self, config, tokenizer_service:TokenizerService) -> None:
        self.docs_path = config["docs"]
        self.qry_path = config["qry"]
        self.rel_path = config["rel"]
        self._tokenizer = tokenizer_service
    
    def get_data(self, PATH_TO_FILE: str):
        NotImplementedError()

    
    def get_txt_data(self):
        NotImplementedError()

    
    def get_qry_data(self):
        NotImplementedError()

    
    def get_rel(self):
        NotImplementedError()

    
    def get_rel_numpy(self):
        NotImplementedError()
