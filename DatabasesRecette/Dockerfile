FROM mysql:8.0.27

WORKDIR /dump

ENV MYSQL_DATABASE recettebis

COPY databasesrecette/DumpDatabases.sql  /docker-entrypoint-initdb.d/

