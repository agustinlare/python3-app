FROM python:3.8.13-buster

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "app.py" ]
ENTRYPOINT [ "python3" ]