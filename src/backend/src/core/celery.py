from celery import Celery
from config import settings

celery = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}",
)
celery.autodiscover_tasks(["mailing.tasks"], force=True)
