from .parser.services import CorpusService


class SearchEngineService:
    def __init__(self, parser_service: CorpusService) -> None:
        self._parser = parser_service