
import databases
import sqlalchemy
import os
from dotenv import load_dotenv
load_dotenv(".env")

# Postgres Database
DATABASE_URL = os.environ["DATABASE_URL"]




DATABASE_URL = os.environ["DATABASE_URL"]
print(DATABASE_URL)
DB_MOTOR = os.environ["DB_MOTOR"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOSTNAME = os.environ["DB_HOSTNAME"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]
PGADMIN_EMAIL = os.environ["PGADMIN_EMAIL"]
PGADMIN_PASSWORD = os.environ["PGADMIN_PASSWORD"]

#DB_MOTOR + DB_USER +":"+DB_PASSWORD +"@" +DB_HOSTNAME +":" +DB_PORT +"/"+DB_NAME
DATABASE_URL = "{}{}:{}@{}:{}/{}".format(
    DB_MOTOR,
    DB_USER,
    DB_PASSWORD,
    DB_HOSTNAME,
    DB_PORT,
    DB_NAME)
print(DATABASE_URL)




database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "py_users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("gender", sqlalchemy.CHAR),
    sqlalchemy.Column("create_at", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.CHAR),
)




engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)
