from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
import csv
from . import transactions as tr
import logging.config

# TODO: enhance configuration
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

@app.get("/transactions", response_model=List[tr.TransactionOutput])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(tr.get_db)):
    transactions = db.query(tr.Transaction).offset(skip).limit(limit).all()
    return [tr.TransactionOutput(**transaction.as_dict()) for transaction in transactions]


# @app.post("/transactions", response_model=List[tr.TransactionOutput])
# def create_transactions(file: UploadFile = File(...), db: Session = Depends(get_db)):
#     transactions = []
#     with file.file as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             transaction = Transaction(**row)
#             db.add(transaction)
#             db.commit()
#             db.refresh(transaction)
#             transactions.append(transaction)
#     return transactions