## Entrega Final Sistemas de Recuperación de Información

### Autor:
- Leandro Hernandez C-312

### Modelos Implementados
- Boolean Model
- Vector Model
- Latent Semantic Indexing


### Datasets utilizados:
- Cranfield
- Cisi
- Medline

### Pre-requisites
```bash
python -m pip install -r requirements.txt
```
### Config
```
[cran]
docs: path/to/cran/docs
qry: path/to/cran/queries
rel: path/to/cran/qry_doc_rel

[med]
...

[cisi]
...

[flask]
host: localhost
port: 3000
```

### Forma de Ejecucion:
```bash
python -m sri
```

### Unit tests:
```bash
python -m pytest
```
