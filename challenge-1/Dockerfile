FROM ubuntu AS base 

# Install build dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    socat

RUN mkdir /challenge

COPY super_service setup-challenge.py /app/
COPY start.sh /app/
WORKDIR /app/
RUN tar czvf /challenge/artifacts.tar.gz super_service

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py

# The start.sh script starts a socat listener on port 5555, that connects to the
# python script.
EXPOSE 5555
# PUBLISH 5555 AS socat

RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]
