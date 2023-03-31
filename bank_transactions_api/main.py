from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import csv
from . import transactions as tr
from .mylogging import log

app = FastAPI()

@app.get("/transactions", response_model=List[tr.TransactionOutput])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(tr.get_db)):
    transactions = db.query(tr.Transaction).offset(skip).limit(limit).all()
    return [tr.TransactionOutput(**transaction.as_dict()) for transaction in transactions]


@app.post("/transactions", response_model=List[tr.TransactionOutput])
def create_transactions(json: List[tr.TransactionInput], db: Session = Depends(tr.get_db)):
    
    transactions: List[tr.TransactionOutput] = []
    try:
        for t_input in json:
            transaction_db = tr.Transaction(**t_input.dict())

            db.add(transaction_db)
            db.commit()
            
            db.refresh(transaction_db)
            transactions.append(tr.TransactionOutput(**transaction_db.as_dict()))
        
        return transactions
    except Exception as e:
        log.error(f"An error has occurred while loading transactions into database: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail=e)