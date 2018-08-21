FROM alpine:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /build
COPY . /build/

RUN apk update && \
  apk add --no-cache gcc musl-dev python3 python3-dev py3-psycopg2 py-pip jpeg-dev zlib-dev openssl-dev libffi-dev

ENV LIBRARY_PATH=/lib:/usr/lib

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt --no-cache-dir
RUN pip install flask-cors --upgrade


ENTRYPOINT ["/bin/sh", "entrypoint.sh"]

