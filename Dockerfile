#syntax=docker/dockerfile:1
# Python version.
FROM python:3-alpine

# This is the directory we're working 
# in inside of the container.
WORKDIR /app

# We pip froze these requirements, now we're 
# going to install them in the container.
COPY requirements.txt requirements.txt

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# Copy everything and run!
COPY . .
CMD ["python3","-m","flask","run","--host=0.0.0.0"]