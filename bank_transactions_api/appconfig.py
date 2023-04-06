import os
from .mylogging import log

host = os.getenv('DB_HOST')
port = int(os.getenv('DB_PORT'))
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')
run_environment = os.getenv('RUN_ENVIRONMENT')
instance_connection_name = os.getenv('INSTANCE_CONNECTION_NAME')

log.debug(f"Configurations read by the api service: user={user}, password={password}, host={host}, port={port}, database={database}, run_environment={run_environment}")