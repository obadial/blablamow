# Blabla Mow
New BlaBlaCar's mow service

## Local requirements
- docker & docker-compose 
- poetry

## Use docker

```sh
cd [BLABLAMOW]
docker-compose build && docker-compose up
```

## BlaBla Mow commands

You can execute BlaBla Mow with :

```sh
python3 ./run.py ./example/subject_test.txt
```

You can lanch tests

```sh
poetry run pytest
```

## Some elements to read

- `Docker`: https://www.docker.com/<br/>
- `Poetry`: https://www.python-poetry.org/docs/<br/>