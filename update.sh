#!/usr/bin/env bash

while true
do
    sha=$(git rev-parse main)
    git pull
    sha2=$(git rev-parse main)

    if [ "$sha" != "$sha2" ]
    then
        docker compose build
        docker compose up -d
    fi

    sleep 3
done
