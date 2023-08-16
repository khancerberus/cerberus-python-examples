FROM python:3.11.4-alpine3.18

ENV PYTHONUNBUFFERED=1

WORKDIR /APP

COPY ./Pipfile ./

RUN env PIPENV_VENV_IN_PROJECT=1 && pip install pipenv && pipenv install

COPY ./ ./

CMD ["pipenv", "run", "python", "app1/run.py"]

EXPOSE 5000
EXPOSE 5432
