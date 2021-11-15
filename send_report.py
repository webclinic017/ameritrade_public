
from datetime import datetime, timedelta
from test_market_options import test_market_options
from find_next_friday import find_next_friday
from send_email import send_email
# from database import insert_data
from db import insert_data
from dotenv import load_dotenv
import os
load_dotenv(".env")


def send_report(candles, symbol, low_rank, high_rank):
    EMAIL = os.environ["EMAIL"]
    time_now = datetime.now()
    inferior_time_limit = time_now - timedelta(minutes=65)
    superior_time_limit = time_now + timedelta(minutes=65)
    for index in range(1, len(candles['open'])):
        if "call" in candles['action_type'][index]:
            if candles.index[index] > inferior_time_limit and candles.index[index] < superior_time_limit:
                dict_of_contract = test_market_options(symbol=symbol,
                                                       contractType="CALL",
                                                       toDate=find_next_friday(),
                                                       low_rank=low_rank,
                                                       high_rank=high_rank
                                                       )
                if not dict_of_contract:
                    subject = "symbol: " + symbol + ", type of action: CALL, " + "time of the request: " + str(time_now) + ', candle time: ' + str(candles.index[index]) + ", condition: " + str(candles['action_type'][index])
                    send_email(EMAIL, subject, dict_of_contract)
                    send_email("eydmax0@gmail.com", subject, dict_of_contract)
                    insert_data(
                        symbol=symbol,
                        candle_date=candles.index[index],
                        open_value=candles['open'][index],
                        close_value=candles['close'][index],
                        action_type=candles['action_type'][index],
                        call_or_put="call",
                        strike=dict_of_contract['strike'],
                        ask_price=dict_of_contract['ask'],
                        bid_price=dict_of_contract['bid'],
                        status_of_action="on posession",
                        order_date=datetime.now())

        if "put" in candles['action_type'][index]:
            if candles.index[index] > inferior_time_limit and candles.index[index] < superior_time_limit:
                dict_of_contract = test_market_options(
                    symbol=symbol,
                    contractType="PUT",
                    toDate=find_next_friday(),
                    low_rank=low_rank,
                    high_rank=high_rank
                )
                if not dict_of_contract:
                    subject = "symbol: " + symbol + ", type of action: PUT, " + "time of the request: " + str(time_now) + ', candle time: ' + str(candles.index[index]) + ", condition: " + str(candles['action_type'][index])
                    send_email(EMAIL, subject, dict_of_contract)
                    send_email("eydmax0@gmail.com", subject, dict_of_contract)
                    insert_data(
                        symbol=symbol,
                        candle_date=candles.index[index],
                        open_value=candles['open'][index],
                        close_value=candles['close'][index],
                        action_type=candles['action_type'][index],
                        call_or_put="put",
                        strike=dict_of_contract['strike'],
                        ask_price=dict_of_contract['ask'],
                        bid_price=dict_of_contract['bid'],
                        status_of_action="on posession",
                        order_date=datetime.now())
