#!/usr/bin/env bash

# Exit when any command fails
set -e

# Run database migrations (if you use Alembic)
if [ -d "alembic" ]; then
  echo "Running Alembic migrations..."
  alembic upgrade head || echo "No Alembic found, skipping migrations"
fi

echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
