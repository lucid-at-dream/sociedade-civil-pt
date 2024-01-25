#!/usr/bin/env bash

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
cd $SCRIPT_DIR


while true
do
    sha=$(git rev-parse main)
    git pull
    sha2=$(git rev-parse main)

    if [ "$sha" != "$sha2" ]
    then
        (cd server && cargo build --release)
        docker compose build
        docker compose up -d
    fi

    sleep 3
done
