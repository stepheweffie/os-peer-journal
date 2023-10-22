# Send an email with the code and link
# You can't name files email.py in flask apps because it conflicts with the email module.
from models import Subscriber


def send_verify_email(code, hash_code, subscriber):
    recipient = Subscriber.query.filter_by(email_hash=subscriber).first()
    address = recipient.email
    name = recipient.name
    email_text = f'Your code is: {code}'
    link = f'http://127.0.0.1:8080/confirm?code={hash_code}'
    print(link)
    message = f'Thank you, for registering with the journal, {name}. {email_text} Please visit {link} to ' \
              f'confirm your email address.'
    print(message)



