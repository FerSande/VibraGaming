FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./pyproject.toml /app
COPY ./poetry.lock /app
COPY ./README.md /app
COPY ./vibraproject/routers/searcher.py /app/vibraproject/routers/searcher.py
COPY ./vibraproject/routers/vibra_challenge.csv /app/vibraproject/routers/vibra_challenge.csv
COPY ./main.py /app

RUN python -m pip install --user --upgrade pip poetry 
RUN python -m poetry install 

EXPOSE 8095

CMD python -m poetry run python /app/main.py