from ..searchengine.services import SearchEngineService

class FlaskService:
    def __init__(self, config, search_engine: SearchEngineService) -> None:
        self.search_engine = search_engine
        self.host = config.host
        self.port = int(config.port)
    