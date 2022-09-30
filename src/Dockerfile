FROM debian:stable-20220622-slim

ENV PORT 8181

RUN apt-get update && \
    apt-get install python3-minimal -y && \
    apt-get install python3-pip -y

WORKDIR /app
COPY . ./

RUN pip install --user pipenv
ENV PATH $PATH:/root/.local/bin
RUN pipenv --python /usr/bin/python3 install -d

ENTRYPOINT ["pipenv", "run", "prod"]
