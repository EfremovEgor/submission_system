#!/bin/bash
echo "Apply database migrations"
alembic upgrade head
echo "Run server"
gunicorn main:app --bind 0.0.0.0:8000 --workers 4 --worker-class uvicorn.workers.UvicornWorker  --log-level debug
# uvicorn main:app --host 0.0.0.0 --port 8000

