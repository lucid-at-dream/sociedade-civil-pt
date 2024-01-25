FROM ubuntu:22.04

WORKDIR /app

COPY . .

EXPOSE 5000

CMD ["/app/server/target/release/server"]

