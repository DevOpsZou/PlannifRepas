FROM python:3.9.10

COPY requirements.txt  requirements.txt
RUN pip install -r requirements.txt
COPY . /
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]