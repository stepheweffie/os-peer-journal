from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()


class NewsletterEmails(Base):
    __tablename__ = 'newsletter_emails'
    id = Column(Integer, Sequence('email_id_seq'), primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)


class UserContactMessage(Base):
    __tablename__ = 'user_contacts'
    id = Column(Integer, Sequence('user_contact_id_seq'), primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    message = Column(String(500))


class SalesContacts(Base):
    __tablename__ = 'sales_contacts'
    id = Column(Integer, Sequence('contact_id_seq'), primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    institution = Column(String(100))
    email = Column(String(100), unique=True)
    phone = Column(String(20), unique=True)
    # city = Column(String(100))
    # state = Column(String(100))
