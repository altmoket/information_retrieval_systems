from .normal import NormalTokenizer


class TokenizerService:
    def __init__(self, normal_tokenizer: NormalTokenizer) -> None:
        self._normal = normal_tokenizer
        self.activate_tokenizer("normal")
    
    def activate_tokenizer(self, tokenizer_type:str = "normal"):
        if tokenizer_type == "normal":
            self._tokenizer = self._normal
        elif tokenizer_type == "boolean":
            self._tokenizer = ...
            
    def tokenize(self, text:str):
        return self._tokenizer.tokenize(text)