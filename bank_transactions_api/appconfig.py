import os
from .mylogging import log

host = os.getenv('MYSQL_HOST')
port = int(os.getenv('MYSQL_PORT'))
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

log.debug(f"Configurations read by the api service: user={user}, password={password}, host={host}, port={port}, database={database}")