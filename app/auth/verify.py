import random
import smtplib
from email.message import EmailMessage
from settings import redis_verify_client
from config import EMAIL_ADDRESS, APP_PASS


def generate_secret_code():
    code = random.randint(100000, 999999)
    return code


def send_code_to_email(email, code):
    msg = EmailMessage()
    msg['Subject'] = 'Email subject'
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

    return True


def verify_email(user_code, entered_code):
    if user_code == entered_code:
        return True
    return False
