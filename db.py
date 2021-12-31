import databases
import sqlalchemy
from sqlalchemy.sql import text
import os
from dotenv import load_dotenv
load_dotenv(".env")

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

# DB_MOTOR + DB_USER +":"+DB_PASSWORD +"@" +DB_HOSTNAME +":" +DB_PORT +"/"+DB_NAME

DATABASE_URL = "{}{}:{}@{}:{}/{}".format(
    DB_MOTOR,
    DB_USER,
    DB_PASSWORD,
    DB_HOSTNAME,
    DB_PORT,
    DB_NAME)
print(DATABASE_URL)

#database = databases.Database(DATABASE_URL)


metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)
database = engine.connect()




register_of_calls_and_puts_actions = sqlalchemy.Table(
    "register_of_calls_and_puts_actions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INT, primary_key=True),
    sqlalchemy.Column("symbol", sqlalchemy.String),
    sqlalchemy.Column("candle_date", sqlalchemy.DateTime),
    sqlalchemy.Column("open_value", sqlalchemy.Float),
    sqlalchemy.Column("close_value", sqlalchemy.Float),
    sqlalchemy.Column("action_type", sqlalchemy.String),
    sqlalchemy.Column("call_or_put", sqlalchemy.String),
    sqlalchemy.Column("strike", sqlalchemy.Float),
    sqlalchemy.Column("ask_price", sqlalchemy.Float),
    sqlalchemy.Column("bid_price", sqlalchemy.Float),
    sqlalchemy.Column("status_of_action", sqlalchemy.String),
    sqlalchemy.Column("order_date", sqlalchemy.DateTime),
)

metadata.create_all(engine)

def insert_data(symbol,
                candle_date,
                open_value,
                close_value,
                action_type,
                call_or_put,
                strike,
                ask_price,
                bid_price,
                status_of_action,
                order_date):
    query = register_of_calls_and_puts_actions.insert().values(
        symbol=symbol,
        candle_date=candle_date,
        open_value=open_value,
        close_value=close_value,
        action_type=action_type,
        call_or_put=call_or_put,
        strike=strike,
        ask_price=ask_price,
        bid_price=bid_price,
        status_of_action=status_of_action,
        order_date=order_date)
    database.execute(query)


def ask_purchases(status, symbol, call_or_put):
    list_of_purchases = []
    query = text(
        "SELECT  register_of_calls_and_puts_actions.symbol, "
        "register_of_calls_and_puts_actions.action_type, register_of_calls_and_puts_actions.candle_date, " 
        "register_of_calls_and_puts_actions.strike , register_of_calls_and_puts_actions.ask_price ,"
        "register_of_calls_and_puts_actions.bid_price,id "
        "FROM  register_of_calls_and_puts_actions "
        "WHERE register_of_calls_and_puts_actions.status_of_action LIKE :status AND "
        "register_of_calls_and_puts_actions.symbol LIKE :symbol AND "
        "register_of_calls_and_puts_actions.call_or_put LIKE :call_or_put"
    )


    records = database.execute(query, {"status": status, "symbol": symbol, "call_or_put": call_or_put}).fetchall()
    records = list(records)
    print(records)
    for record in records:
        print(record)
        list_of_purchases.append(record)

    return list_of_purchases


async def update_status_of_actions(strike, id):
    query = register_of_calls_and_puts_actions.update(). \
        where(register_of_calls_and_puts_actions.c.id == id).\
        values(status_of_actions="selled", strike=strike)
    await database.execute(query)




if __name__ == '__main__':
    from datetime import datetime
    insert_data(symbol="AAPL",
                candle_date="2021-10-04 09:30:00",
                open_value=1.1,
                close_value=2.2,
                action_type="put condition 1",
                call_or_put="put",
                strike=3.3,
                ask_price=4.4,
                bid_price=5.5,
                status_of_action="on posession",
                order_date=datetime.now())

    ask_purchases(status="on posession", symbol="AAPL", call_or_put="call")

"""

register_of_calls_and_puts_actions.c.symbol,
register_of_calls_and_puts_actions.c.action_type,
register_of_calls_and_puts_actions.c.candle_date,
register_of_calls_and_puts_actions.c.strike,
register_of_calls_and_puts_actions.c.ask_price,
register_of_calls_and_puts_actions.c.bid_price,
register_of_calls_and_puts_actions.c.id]
"""
