#!/bin/sh

IMAGE_NAME="daily-tg-bot"
CONTAINER_NAME="daily-tg-bot"

if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Removing existing container: $CONTAINER_NAME"
    docker rm -f $CONTAINER_NAME
fi

if [ "$(docker images -q $IMAGE_NAME)" ]; then
    echo "Removing existing image: $IMAGE_NAME"
    docker rmi -f $IMAGE_NAME
fi

echo "Building Docker image"
docker build -t $IMAGE_NAME . --no-cache

echo "Running container in detached mode"
docker run -d --name $CONTAINER_NAME --env-file .env $IMAGE_NAME

