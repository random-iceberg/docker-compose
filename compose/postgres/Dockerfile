# In order to avoid bind-mounts, pass postgres config files by building an image
FROM postgres:17-alpine
COPY ./initdb.d /docker-entrypoint-initdb.d
RUN find /docker-entrypoint-initdb.d -type f -exec dos2unix {} \;