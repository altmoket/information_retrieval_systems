from ..searchengine.services import SearchEngineService
from flask import Flask, request
# from .routes import show_forms
import json
class NavigatorService:
    def __init__(self, config, search_engine: SearchEngineService) -> None:
        self.search_engine = search_engine
        self.host = config['host']
        self.port = int(config['port'])
        
    def run(self):
        app = self._create_app()
        app.run(host=self.host, port=self.port)
    
    def _create_app(self):
        app = Flask(__name__)
        app.config['SECRET_KEY'] = '47d1b623279795a1a5f2cab925d5ae693be3ed21497b4979'
        app.add_url_rule(rule='/api/run_code', view_func=self.run_query, methods=['POST'])
        return app
    
    async def run_query(self):
        query = request.headers['query']
        model = request.headers['model'] or "VectorModel"
        corpus = request.headers['corpus'] or "cranfield"
        suavizado = request.headers['suavizado'] or 0.5
        umbral = request.headers['umbral'] or 0.7
        limit = request.headers['limit'] or 30
        self.search_engine.set_model_and_corpus(model_name=model, corpus_name=corpus)
        results = self.search_engine.run_query(query, umbral, limit, suavizado)
        return json.dumps(results, indent=4, sort_keys=False)
    
    