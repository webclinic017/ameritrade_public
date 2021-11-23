import time

import uvicorn
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware
import models as mdUser
from db import database, register_of_calls_and_puts_actions
import datetime
import uuid
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
from datetime import datetime, timedelta
# import to avoid errors of threads
import matplotlib.pyplot as mpl
mpl.switch_backend('agg')

import mplfinance as mpf
from threading import Thread
import queue

from get_price_history import get_price_history
from classify_candles import classify_candles
from get_hammers import get_hammers
from get_gap import get_gap
from get_max_and_min import get_max_and_min
from graph_max_and_min import graph_max_and_min
from table_type_actions import table_type_actions
from max_and_min_comparison import max_and_min_comparasion
from check_trend import check_trend
from check_lateral_trend import check_lateral_trend
from search_for_roof_and_floor import search_for_roof_and_floor
from get_action_call import get_action_call
from get_action_put import get_action_put
from get_real_time_data import get_real_time_data
from send_report import send_report
from stop_conditions import stop_conditions
from get_price_history_poligon import get_price_history_poligon
from run_automatic_request import automatic_request
from db import insert_data, ask_purchases


load_dotenv(".env")
app = FastAPI()
#app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.mount("/static", StaticFiles(directory="static"), name="/static")
templates = Jinja2Templates(directory="templates")

def create_graph(symbol, period, periodType, frecuencyType, frecuency, cola, low_rank, high_rank):
    pd.options.mode.chained_assignment = None
    img = "static/assets/img/{}.png".format(symbol)
    title = "{} prices (Last {} days)".format(symbol, period)

    # candles = get_price_history(symbol=symbol, period=period, periodType=periodType, frecuencyType=frecuencyType, frecuency=frecuency)
    today = datetime.today()
    ten_days_ago = today - timedelta(days=15)
    ten_days_ago = datetime.strftime(ten_days_ago, '%Y-%m-%d')
    one_day_ago = today - timedelta(days=1)
    one_day_ago = datetime.strftime(one_day_ago, '%Y-%m-%d')
    today = datetime.strftime(today, '%Y-%m-%d')
    candles = get_price_history_poligon(symbol=symbol, multiplier="60", timespan="minute", from_date=ten_days_ago,
                                        to_date=one_day_ago)

    try:
        time_now = datetime.now()
        if time_now.hour >= 9:
            candles_real_time = get_real_time_data(symbol=symbol, multiplier="60", timespan="minute", from_date=today,
                                                   to_date=today)
            candles = candles.append(candles_real_time)
    except:
        print("dia no laboral")
    # pd.set_option('display.max_rows', candles.shape[0]+1)
    # print(candles)
    candles = classify_candles(candles)
    candles = get_hammers(candles)
    candles = get_gap(candles)
    candles = get_max_and_min(candles)
    max,min = graph_max_and_min(candles)
    candles = max_and_min_comparasion(candles)
    candles = check_trend(candles)
    candles = check_lateral_trend(candles)
    candles = search_for_roof_and_floor(candles)
    candles = get_action_call(candles)
    candles = get_action_put(candles)
    send_report(candles, symbol, low_rank, high_rank)
    stop_conditions(candles, symbol)

    table_type_actions(candles, cola)
    apds = [
        mpf.make_addplot(max, type='scatter', markersize=10, color='r', marker='^'),
        mpf.make_addplot(min, type='scatter', markersize=10, color='g', marker='v'),
    ]

    mpf.plot(candles, addplot=apds, type='candle', title=title, style='charles', savefig=img)


@app.get("/", response_class=HTMLResponse)

async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/apple", response_class=HTMLResponse)
async def apple(request: Request):
    img = "static/assets/img/AAPL.png"
    cola = queue.LifoQueue()
    create_graph_thread = Thread(target=create_graph, args=("AAPL", 10, 'day', 'minute', '30', cola, 0, .80))
    create_graph_thread.start()
    data = cola.get()
    return templates.TemplateResponse("apple.html", {"request": request, "img":img,"data":data})

@app.get("/amazon", response_class=HTMLResponse)
async def amazon(request: Request):
    img = "static/assets/img/AMZN.png"
    cola = queue.LifoQueue()
    create_graph_thread = Thread(target=create_graph, args=("AMZN", 10, 'day', 'minute', '30', cola, 0, .80))
    create_graph_thread.start()
    data = cola.get()
    return templates.TemplateResponse("amazon.html", {"request": request, "img":img,"data":data})



@app.get("/bank_of_america", response_class=HTMLResponse)
async def bank_of_america(request: Request):
    img = "static/assets/img/BAC.png"
    cola = queue.LifoQueue()
    create_graph_thread = Thread(target=create_graph, args=("BAC", 10, 'day', 'minute', '30', cola, 0, .80))
    create_graph_thread.start()
    data = cola.get()
    return templates.TemplateResponse("bank_of_america.html", {"request": request, "img":img,"data":data})

@app.get("/facebook", response_class=HTMLResponse)
async def facebook(request: Request):
    img = "static/assets/img/FB.png"
    cola = queue.LifoQueue()
    create_graph_thread = Thread(target=create_graph, args=("FB", 10, 'day', 'minute', '30', cola, 0, .80))
    create_graph_thread.start()
    data = cola.get()
    return templates.TemplateResponse("facebook.html", {"request": request, "img":img,"data":data})

@app.get("/moderna", response_class=HTMLResponse)
async def moderna(request: Request):
    img = "static/assets/img/MRNA.png"
    cola = queue.LifoQueue()
    create_graph_thread = Thread(target=create_graph, args=("MRNA", 10, 'day', 'minute', '30', cola, 0, .80))
    create_graph_thread.start()
    data = cola.get()
    return templates.TemplateResponse("moderna.html", {"request": request, "img":img,"data":data})



@app.on_event("startup")
async def startup():
    thread_automatic_request = Thread(target=automatic_request)
    thread_automatic_request.start()
    await database.connect()
    time.sleep(5)
    print("inserting data")
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
    print("finishing insert data and asking for purchases")
    print(await ask_purchases(status="on posession", symbol="AAPL", call_or_put="put"))
    print("finishing asking purchases")
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

"""
@app.get("/users", response_model=List[mdUser.UserList], tags=["Users"])
async def find_all_users():
    query = users.select()
    return await database.fetch_all(query)


@app.post("/users", response_model=mdUser.UserList, tags=["Users"])
async def register_user(user: mdUser.UserEntry):
    gID = str(uuid.uuid1())
    gDate = str(datetime.datetime.now())
    query = users.insert().values(
        id=gID,
        username=user.username,
        password=user.password,
        first_name=user.first_name,
        last_name=user.last_name,
        gender=user.gender,
        create_at=gDate,
        status="1"
    )

    await database.execute(query)
    return {
        "id": gID,
        **user.dict(),
        "create_at": gDate,
        "status": "1"
    }


@app.get("/users/{userId}", response_model=mdUser.UserList, tags=["Users"])
async def find_user_by_id(userId: str):
    query = users.select().where(users.c.id == userId)
    return await database.fetch_one(query)


@app.put("/users", response_model=mdUser.UserList, tags=["Users"])
async def update_user(user: mdUser.UserUpdate):
    gDate = str(datetime.datetime.now())
    query = users.update().\
        where(users.c.id == user.id).\
        values(
            first_name=user.first_name,
            last_name=user.last_name,
            gender=user.gender,
            status=user.status,
            create_at=gDate,
        )
    await database.execute(query)
    return await find_user_by_id(user.id)


@app.delete("/users/{userId}", tags=["Users"])
async def delete_user(user: mdUser.UserDelete):
    query = users.delete().where(users.c.id == user.id)
    await database.execute(query)
    return {
        "status": True,
        "message": "This user has been deleted successfully."
    }
"""


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
