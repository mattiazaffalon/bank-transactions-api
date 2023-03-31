from typing import List
from datetime import date, datetime
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .appconfig import user, password, host, port, database

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

def get_db():
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
    with Session() as session:
        try:
            yield session
        finally:
            session.close()

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    transaction_date = Column(Date)
    value_date = Column(Date)
    value = Column(Numeric)
    description = Column(String(255))
    direction = Column(String(255))
    amount = Column(Numeric)
    transaction_year = Column(Integer)
    transaction_month = Column(Integer)
    transaction_monthday = Column(Integer)
    transaction_dayofweek = Column(String(255))
    transaction_month_id = Column(String(255))
    value_year = Column(Integer)
    value_month = Column(Integer)
    value_monthday = Column(Integer)
    value_dayofweek = Column(String(255))
    value_month_id = Column(String(255))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TransactionInput(BaseModel):
    transaction_date: date
    value_date: date
    value: float
    description: str
    direction: str
    amount: float
    transaction_year: int
    transaction_month: int
    transaction_monthday: int
    transaction_dayofweek: str
    transaction_month_id: str
    value_year: int
    value_month: int
    value_monthday: int
    value_dayofweek: str
    value_month_id: str


class TransactionOutput(BaseModel):
    id: int
    transaction_date: date
    value_date: date
    value: float
    description: str
    direction: str
    amount: float
    transaction_year: int
    transaction_month: int
    transaction_monthday: int
    transaction_dayofweek: str
    transaction_month_id: str
    value_year: int
    value_month: int
    value_monthday: int
    value_dayofweek: str
    value_month_id: str


Base.metadata.create_all(bind=engine)