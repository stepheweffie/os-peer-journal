from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import NewsletterEmails, SalesContacts, UserContactMessage  # Assuming you have models.py with your SQLAlchemy models

DATABASE_URL = "sqlite:///./leads.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def add_email_subscription(name, address):
    db_session = SessionLocal()
    try:
        new_newsletter_email = NewsletterEmails(name=name, email=address)
        db_session.add(new_newsletter_email)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        return str(e)
    finally:
        db_session.close()


def add_user_contact(name, email, message):
    db_session = SessionLocal()
    try:
        new_user_contact = UserContactMessage(name=name, email=email, message=message)
        db_session.add(new_user_contact)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        return str(e)
    finally:
        db_session.close()


def add_sales_contact(first_name, last_name, institution, email, phone):
    db_session = SessionLocal()
    try:
        new_contact = SalesContacts(first_name=first_name, last_name=last_name, email=email, institution=institution,
                                    phone=phone)
        db_session.add(new_contact)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        return str(e)
    finally:
        db_session.close()
