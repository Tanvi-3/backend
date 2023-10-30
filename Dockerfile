FROM docker.io/python:3.10

WORKDIR /

# --- [Install python and pip] ---
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3 python3-pip git
COPY . /

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

<<<<<<< HEAD
ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8069"

EXPOSE 8069
=======
ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8080"

EXPOSE 8080
>>>>>>> d40f02080a3024b19dbb594094b327aaf34b9c5b

CMD [ "gunicorn", "main:app" ]
