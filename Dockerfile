FROM python:3.7-buster

RUN adduser -D findmyuni

WORKDIR /home/findmyuni

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential

COPY config config
COPY database database
COPY elastic elastic
COPY flask-mongoengine flask-mongoengine
COPY instance instance
COPY university university
COPY user user
COPY __init__.py Pipfile Pipfile.lock run.py setup.sh startup.sh ./

RUN chmod +x setup.sh
RUN chmod +x startup.sh

RUN chown -R findmyuni:findmyuni ./
USER findmyuni

EXPOSE 5000
ENTRYPOINT ["./startup.sh"]

# to do: install mongodb, elastic as docker