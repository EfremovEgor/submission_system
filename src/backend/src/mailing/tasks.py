import asyncio
from users.schemas import UserBase
from submissions.schemas import SubmissionInDBBase

from mailing.service import Email
from core.celery import celery
from pydantic import EmailStr, HttpUrl

from .schemas import SubmissionEmailData

loop = asyncio.get_event_loop()


@celery.task
def send_confirmation_email(email: EmailStr, url: HttpUrl):
    loop.run_until_complete(
        Email.send_confirmation_email(
            email,
            url,
        )
    )


@celery.task
def send_create_submission_email(email: EmailStr, data: SubmissionEmailData):
    loop.run_until_complete(Email.send_create_submission_email(email, data))


@celery.task
def send_update_submission_email(email: EmailStr, data: SubmissionEmailData):
    loop.run_until_complete(Email.send_update_submission_email(email, data))
