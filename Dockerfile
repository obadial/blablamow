FROM python:3.8-slim-buster as builder
RUN pip install --upgrade pip
RUN apt-get update && apt-get -y install gcc
RUN pip install poetry
WORKDIR /blablamow

COPY . .
COPY pyproject.toml poetry.lock /blablamow/
RUN poetry install
RUN poetry build
RUN poetry export -f requirements.txt -o  requirements.txt

FROM builder

RUN pip install -r requirements.txt
RUN pip install dist/*.whl

CMD ["python3", "./run.py", "./example/subject_test.txt"]
