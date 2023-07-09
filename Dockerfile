FROM python:3.8.13-buster

ARG EXPOSED_PORT
ENV EXPOSED_PORT=${EXPOSED_PORT}

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE ${EXPOSED_PORT}

CMD [ "app.py" ]
ENTRYPOINT [ "python3" ]