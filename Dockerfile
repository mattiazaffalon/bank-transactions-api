FROM python:3.8 AS builder

WORKDIR /build

COPY . .
RUN pip install -e .

CMD ["uvicorn", "bank_transactions_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
