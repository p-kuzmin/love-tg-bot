#!/bin/sh

if [ "$(docker ps -aq -f name=daily-tg-bot)" ]; then
    echo "Removing existing container: daily-tg-bot"
    docker rm -f daily-tg-bot
fi

echo "Building Docker image"
docker build -t daily-tg-bot . --no-cache

echo "Running container"
docker run --name daily-tg-bot --env-file .env daily-tg-bot
