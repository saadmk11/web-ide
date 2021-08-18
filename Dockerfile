FROM docker:19.03.13

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apk update \
    && apk add --no-cache \
       py-pip \
       gcc \
       python3-dev \
       libressl-dev \
       musl-dev \
       libffi-dev \
       openssl-dev \
       cargo

RUN pip install --no-cache-dir --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
