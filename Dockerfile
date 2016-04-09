FROM python:2.7.10

RUN apt-get update && apt-get install -y \
    locales && \
    echo "cs_CZ.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

ENTRYPOINT ["/usr/bin/make"]

VOLUME /src
WORKDIR /src

RUN pip install  \
    markdown==2.6.2 \
    typogrify==2.0.7 \
    pelican==3.6.3
