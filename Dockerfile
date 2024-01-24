FROM python:3.12.1-bookworm

WORKDIR /app

COPY server/requirements.txt .
RUN pip install -r requirements.txt && rm -f requirements.txt

