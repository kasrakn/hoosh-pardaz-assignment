# syntax=docker/dockerfile:1
FROM python:3.10.5-slim-buster

# Set the working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY ./entrypoint.sh /app/entrypoint.sh

# Copy all the fiels in the current directory into the working directory of image
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

# Tell docker what command we want to run when our image is executed inside a container
# This command will be executed in the docker-compsoe, therefore it's been commented here.
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "shipmentTracker.wsgi"]