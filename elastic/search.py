from flask import current_app


def add_to_index(index, model):
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, id=model.id, body=payload, request_timeout=60)


def remove_from_index(index, model):
    current_app.elasticsearch.delete(index=index, id=model.id, request_timeout=60)


def query_index(index, body):
    search = current_app.elasticsearch.search(index=index, body=body, request_timeout=60)
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']['value']
