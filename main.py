# main.py
# Import FastAPI
from fastapi import FastAPI

# Initialize the app
app = FastAPI()

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message" : "Welcome to Bank Transactions api"}
