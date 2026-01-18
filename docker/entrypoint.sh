#!/bin/bash
set -e

echo "Waiting for database..."
DB_HOST=${DB_HOST:-db}
DB_PORT=${DB_PORT:-5432}
MAX_RETRIES=30
RETRY_COUNT=0

while ! nc -z $DB_HOST $DB_PORT; do
  RETRY_COUNT=$((RETRY_COUNT + 1))
  if [ $RETRY_COUNT -ge $MAX_RETRIES ]; then
    echo "Error: Database at $DB_HOST:$DB_PORT is not available after $MAX_RETRIES attempts"
    exit 1
  fi
  echo "Attempt $RETRY_COUNT/$MAX_RETRIES: Database not ready, waiting..."
  sleep 1
done
echo "Database is ready!"

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting application..."
exec "$@"
