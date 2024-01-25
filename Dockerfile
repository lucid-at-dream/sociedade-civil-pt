FROM ubuntu:22.04

WORKDIR /app

COPY . .

CMD ["/app/server/target/release/server"]

