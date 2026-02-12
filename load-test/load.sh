#!/bin/bash

SERVICE_URL=$1

if [ -z "$SERVICE_URL" ]; then
  echo "Usage: ./load.sh <service-url>"
  exit 1
fi

while true
do
  curl $SERVICE_URL/load &
done
