FROM docker.io/python:3.13-slim-bookworm

RUN apt-get update && apt-get upgrade -y && apt-get install -y gcc

RUN useradd -rm -d /home/switch -s /bin/bash -u 2001 switch
RUN mkdir -p /code/switch
RUN chown switch:switch /code/switch

USER switch

RUN pip install --user --no-cache-dir poetry==2.1.4

ENV PATH="/home/switch/.local/bin:${PATH}"

WORKDIR /code

COPY poetry.lock pyproject.toml README.md /code/
COPY src/ /code/src/

RUN poetry install

CMD ["poetry", \
    "run", \
    "uvicorn", \
    "src.vacuum_floor_switch.main:app", \
    "--host", "0.0.0.0", \
    "--port", "8080"]