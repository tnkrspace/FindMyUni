from elasticsearch import Elasticsearch


def elastic_init(app):
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URI']])
