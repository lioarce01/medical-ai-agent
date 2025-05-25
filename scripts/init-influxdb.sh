#!/bin/sh

echo "Waiting for InfluxDB to be ready..."
until curl -s http://influxdb:8086/ping; do
  sleep 1
done

echo "Creating database..."
curl -i -XPOST http://influxdb:8086/query --data-urlencode "q=CREATE DATABASE medical_data" \
  --user admin:admin
