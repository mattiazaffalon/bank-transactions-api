# bank-transactions-api

## Install app locally
```bash
pip install -e .
```

## Local run through python interpreter
Run mysql on docker
```bash
sudo docker run --name my-mysql -p 3306:3306 --env-file .env-local  -d mysql:latest
```


```bash
# Export variables
export $(cat .env-local | xargs) && uvicorn bank_transactions_api.main:app --reload
```

## Local run through docker-compose
```bash
sudo docker-compose --env-file .env-compose up
```

## Sample api calls
```bash
curl -X POST -H "Content-Type: application/json" -d @data/transactions_sample.json http://localhost:8000/transactions
```