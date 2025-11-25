#!/usr/bin/env bash
set -e
# run migrations if present
if [ -d "alembic" ]; then
  echo "Running Alembic migrations..."
  alembic upgrade head || true
fi
echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
