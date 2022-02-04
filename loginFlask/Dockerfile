FROM python:3.9.10

WORKDIR /app

COPY loginFlask/Dockerfile /app/requirements.txt


RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]