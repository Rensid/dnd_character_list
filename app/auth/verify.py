import random
import smtplib
from email.message import EmailMessage
from settings import redis_verify_client
from config import EMAIL_ADDRESS, APP_PASS
from celery import shared_task


def generate_secret_code():
    code = random.randint(100000, 999999)
    return code


@shared_task
def send_code_to_email(email, code):
    msg = EmailMessage()
    msg['Subject'] = 'Email verification'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg.set_content(
        f"""\
        Thank you for registration.

        Your verification code: {code}.

        Please enter this code in the appropriate field.
    """
    )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, APP_PASS)
        smtp.send_message(msg)
