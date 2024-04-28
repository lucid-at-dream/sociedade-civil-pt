FROM postgis/postgis:14-3.4

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Lisbon

USER root

RUN apt -y update && apt install -y gnupg lsb-release wget

RUN echo "deb https://packagecloud.io/timescale/timescaledb/debian/ $(lsb_release -c -s) main" | tee /etc/apt/sources.list.d/timescaledb.list

RUN wget --quiet -O - https://packagecloud.io/timescale/timescaledb/gpgkey | apt-key add -

RUN apt update -y && apt install -y timescaledb-2-postgresql-14

RUN echo "timescaledb-tune --quiet --yes" > /docker-entrypoint-initdb.d/90_timescale.sh

USER postgres
