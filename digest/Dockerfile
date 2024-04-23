FROM ubuntu:22.04

# Install libtorch
RUN apt update && apt install -y python3 python3-pip
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

WORKDIR /app

COPY . .

EXPOSE 5000

CMD ["/app/server/target/release/server"]

