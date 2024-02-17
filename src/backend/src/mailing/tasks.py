import asyncio
from mailing.service import Email
from core.celery import celery
from pydantic import EmailStr, HttpUrl

loop = asyncio.get_event_loop()


@celery.task
def send_confirmation_email(email: EmailStr, url: HttpUrl):
    loop.run_until_complete(
        Email.send_confirmation_email(
            email,
            url,
        )
    )
