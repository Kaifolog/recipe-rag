FROM python:3.9.19-slim-bullseye

# set work directory
WORKDIR /usr/src/recipe-rag

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update
RUN pip install --upgrade pip
COPY ./ ./recipe-rag
RUN pip install -r ./recipe-rag/requirements.txt
WORKDIR /usr/src/recipe-rag/recipe-rag