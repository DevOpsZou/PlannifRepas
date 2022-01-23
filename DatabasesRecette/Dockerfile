FROM mysql:8.0.27

WORKDIR /dump

ENV MYSQL_DATABASE recettebis

COPY DumpDatabases.sql /docker-entrypoint-initdb.d/

