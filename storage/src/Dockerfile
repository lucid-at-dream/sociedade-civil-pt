FROM python:3.12-alpine

COPY Requirements.txt /Requirements.txt
RUN pip install -r /Requirements.txt && rm -f /Requirements.txt

WORKDIR /app

COPY . .

CMD ["flask", "--app", "map", "run", "-h", "0.0.0.0", "-p", "8080", "--debugger"]