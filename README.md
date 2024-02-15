# Fast Transformer
Simplifying transformer model integration into FastAPI applications for seamless NLP development.

#### Simplified microservice approach to deploy models with fastAPI wrapper
## Uses transformer and pytorch (support for configuring tensorflow coming soon..)

### Prerequisite
- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/)
# Running in local

```shell
uvicorn app.main:app 
```
If everything is fine, you should be able to see output as below
```shell
INFO:     Started server process [38901]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

example request
```shell
curl --location 'http://localhost:8000/analyze-sentiments/' \
--header 'Content-Type: application/json' \
--data '["bad programmer"]'
```
example response
```json
[
    {
        "label": "LABEL_1",
        "score": 0.5389513969421387
    }
]
```

### Includes **Dockerfile** - deploy as a microservice in cloud / kubernetes

## Configuration
1. use MODEL_NAME env variable to use different model, no need of re creating image 
```shell
export MODEL_NAME="distilbert-base-uncased"
```