from .containers import SriContainer
from .searchengine.services import SearchEngineService
from dependency_injector.wiring import inject, Provide

@inject
def main(search_engine_service: SearchEngineService = Provide[SriContainer.search_engine_package.search_engine_service]):
    model_name = "VectorModel"
    collection_name = "cranfield"
    query = " what problems of heat conduction in composite slabs have been solved so far . "
    search_engine_service.set_model_and_corpus(model_name, collection_name)
    ranking = search_engine_service.get_ranking(query)
    print(ranking)

if __name__ == "__main__":
    app = SriContainer()
    app.config.from_ini('./config.ini', required=True)
    app.wire(modules=[__name__])
    
    main()


