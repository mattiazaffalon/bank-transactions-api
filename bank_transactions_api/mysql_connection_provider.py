import os

from google.cloud.sql.connector import Connector, IPTypes
from .appconfig import user, password, host, port, database, run_environment, instance_connection_name
import pymysql
import sqlalchemy
from .mylogging import log


def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    log.info("Creating connection through cloud sql python connector")

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    connector = Connector(ip_type)

    def getconn() -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = connector.connect(
            instance_connection_name,
            "pymysql",
            user=user,
            password=password,
            db=database,
        )
        return conn

    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )
    return pool


def create_engine():
    log.info("Creating connection through mysqlconnector (local configuration)")
    SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return create_engine(SQLALCHEMY_DATABASE_URL)


connection_provider = connect_with_connector if run_environment == 'gcp' else create_engine
