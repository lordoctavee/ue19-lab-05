FROM ubuntu:latest
LABEL authors="malis"

ENTRYPOINT ["top", "-b"]