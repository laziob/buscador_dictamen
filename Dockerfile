FROM tiangolo/meinheld-gunicorn-flask:python3.7

#RUN adduser -D buscador

WORKDIR /home/buscador_dictamenes

COPY requirements.txt requirements.txt
RUN python -m venv env
RUN env/bin/pip3 install --upgrade pip
RUN env/bin/pip3 install -r requirements.txt

COPY app.py .
COPY static static
COPY templates templates

ENV FLASK_APP app.py
ENV PORT 80

#USER buscador

EXPOSE 80
CMD env/bin/gunicorn --bind :$PORT --workers 2 --threads 8 app:app