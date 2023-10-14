from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import NewsletterEmails, SalesContacts  # Assuming you have models.py with your SQLAlchemy models

DATABASE_URL = "sqlite:///./leads.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def add_email(address):
    db_session = SessionLocal()
    try:
        new_email = NewsletterEmails(email=address)
        db_session.add(new_email)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        return str(e)
    finally:
        db_session.close()


def add_contact(first_name, last_name, institution, email, phone):
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
