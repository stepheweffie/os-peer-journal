# user = Subscriber.query.filter_by(verify_code=subscriber).first()
# email = user.email
# name = user.name
# Send an email with the code and link
# You can't name files email.py in flask apps because it conflicts with the email module.
def send_verify_email(address, message):
    if address and message:
        return True