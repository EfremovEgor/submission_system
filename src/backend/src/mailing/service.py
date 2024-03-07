from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, HttpUrl
from submissions.models import Submission
from users.models import User
from config import settings
from jinja2 import Environment, select_autoescape, PackageLoader, Template

env = Environment(
    loader=PackageLoader("mailing", "mailing_templates"),
    autoescape=select_autoescape(["html", "xml"]),
)


class Email:
    conf = ConnectionConfig(
        MAIL_USERNAME=settings.EMAIL_USERNAME,
        MAIL_PASSWORD=settings.EMAIL_PASSWORD,
        MAIL_FROM=settings.EMAIL_FROM,
        MAIL_PORT=settings.EMAIL_PORT,
        MAIL_SERVER=settings.EMAIL_HOST,
        MAIL_STARTTLS=settings.EMAIL_STARTTLS,
        MAIL_SSL_TLS=settings.EMAIL_SSL_TLS,
        USE_CREDENTIALS=settings.USE_CREDENTIALS,
        VALIDATE_CERTS=settings.VALIDATE_CERTS,
    )

    @classmethod
    async def send_email(
        cls,
        subject: str,
        template: str,
        emails: list[EmailStr],
        **content: dict,
    ):

        template = env.get_template(f"{template}.html")
        html = template.render(**content)

        message = MessageSchema(
            subject=subject, recipients=emails, body=html, subtype="html"
        )

        fm = FastMail(cls.conf)

        await fm.send_message(message)

    @classmethod
    async def send_confirmation_email(
        cls,
        email: EmailStr,
        url: HttpUrl,
    ):
        await cls.send_email(
            "Your verification code",
            "verification",
            [email],
            url=url,
        )

    @classmethod
    async def send_submission_email(cls, email: EmailStr, submission_data, user):
        await cls.send_email(
            "Submission has been created",
            "submission",
            [email],
            submission_data=submission_data,
            user=user,
        )
