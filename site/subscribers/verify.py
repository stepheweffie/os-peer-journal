# Send an email with the code and link
# You can't name files email.py in flask apps because it conflicts with the email module.
from models import Subscriber
import os
import resend

resend.api_key = os.environ["RESEND_API_KEY"]


def send_verify_email(code, hash_code, subscriber):
    recipient = Subscriber.query.filter_by(email_hash=subscriber).first()
    address = recipient.email
    name = recipient.name
    email_text = f'Your code is: {code}'
    link = f'http://127.0.0.1:8080/confirm?code={hash_code}'
    message = f'Thank you, for registering with the journal, {name}. {email_text} Please visit {link} to ' \
              f'confirm your email address.'
    params = {
        "from": "Acme <onboarding@resend.dev>",
        "to": [f"{address}"],
        "subject": "Please Confirm",
        "html": f"<strong>{message}</strong>",
    }
    email = resend.Emails.send(params)
    print(email)



