FROM mysql:8.0.27
WORKDIR /dump
ENV MYSQL_DATABASE recettebis

COPY Dump20220111.sql /docker-entrypoint-initdb.d/

