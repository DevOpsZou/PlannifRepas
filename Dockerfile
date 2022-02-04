FROM python:3.9.10
# COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app

# RUN pip install -r requirements.txt

# COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]