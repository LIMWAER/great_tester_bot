# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app
ARG PGHOST
ENV PGHOST ${PGHOST}
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["python3"]
CMD ["app.py"]