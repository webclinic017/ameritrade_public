

import requests 
import datetime
import pandas as pd 
import json


import pytz


from dotenv import load_dotenv
import os
load_dotenv(".env")

def get_price_history(**kwargs):


    key = os.environ["API_KEY_AMERITRADE"]
    params = {}
    candles_9_to_16 = []
    params.update({'apikey':key})
    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)

    url = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory?apikey={}&periodType={}&period={}&frequencyType={}&frequency={}".format(
        params['symbol'],
        params['apikey'],
        params['periodType'],
        params['period'],
        params['frecuencyType'],
        params['frecuency']

    )
    response =requests.get(url).json()

    
    for candle in  response['candles']:
        ms = candle['datetime']
        tz_new_york = pytz.timezone("America/New_York")
        tz_mexico = pytz.timezone('America/Mexico_City')
        candle['datetime']=datetime.datetime.fromtimestamp(ms/1000.0, tz_new_york)
        #print('new york: {}  mexico : {}'.format(candle['datetime'], datetime.datetime.fromtimestamp(ms/1000.0, tz_mexico)  ) )
        time_start = candle['datetime'].replace(hour=9, minute=0, second=0, microsecond=0)
        time_stop  = candle['datetime'].replace(hour=16, minute=0, second=0, microsecond=0)
        if candle['datetime'] >= time_start and  candle['datetime'] <= time_stop:
            candle['datetime']=str(datetime.datetime.fromtimestamp(ms/1000.0))
            candles_9_to_16.append(candle)

    
    df = pd.read_json(json.dumps(candles_9_to_16))
    df = df.set_index(pd.DatetimeIndex(df['datetime']))
    df = df.drop(['datetime'], axis=1)

    return df 

