# bank-transactions-api

## Install app locally
```bash
pip install -e .
```

## Local run through python interpreter
Run mysql on docker
```bash
sudo docker run --name my-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=bank_transactions -e MYSQL_USER=mattia -e MYSQL_PASSWORD=mattia -d mysql:latest
```


```bash
# Export variables
export $(cat .env_local | xargs) && uvicorn bank_transactions_api.main:app --reload
```

## Local run through docker-compose
```bash
sudo docker-compose --env-file .env up
```