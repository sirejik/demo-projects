from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    authentication = relationship("Authentication", uselist=False, back_populates=__tablename__)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Authentication(Base):
    __tablename__ = 'authentication'

    account_id = Column(Integer, ForeignKey("account.id", ondelete='CASCADE'), nullable=False, primary_key=True)
    login = Column(String(50), nullable=False)
    password = Column(String(), nullable=False)
    account = relationship("Account", uselist=False, back_populates=__tablename__)

    def __init__(self, login, password, account):
        self.login = login
        self.password = password
        self.account = account


def create_tables_by_models_if_not_exist(db_engine):
    Base.metadata.create_all(db_engine)
