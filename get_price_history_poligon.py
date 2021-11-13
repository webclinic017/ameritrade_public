import requests 
import datetime
import pandas as pd 
import json


import pytz

from dotenv import load_dotenv
import os
load_dotenv(".env")

def get_price_history_poligon(**kwargs):

    key = os.environ["API_KEY_POLYGON"]
    params = {}
   
    params.update({'apikey':key})
    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)

    

    url="https://api.polygon.io/v2/aggs/ticker/{}/range/{}/{}/{}/{}?adjusted=false&sort=asc&apiKey={}&limit=5000".format(
        params['symbol'],
        params['multiplier'],
        params['timespan'],
        params['from_date'],
        params['to_date'],
        params['apikey']

    )
    response =requests.get(url).json()
    candles_9_to_16 =[]
    
    for candle in  response['results']:

        ms = candle['t']
        tz_new_york = pytz.timezone("America/New_York")
        tz_mexico = pytz.timezone('America/Mexico_City')
        candle['t']=datetime.datetime.fromtimestamp(ms/1000.0, tz_new_york)
        #print('new york: {}  mexico : {}'.format(candle['datetime'], datetime.datetime.fromtimestamp(ms/1000.0, tz_mexico)  ) )
        time_start = candle['t'].replace(hour=9, minute=0, second=0, microsecond=0)
        time_stop  = candle['t'].replace(hour=16, minute=0, second=0, microsecond=0)
        if candle['t'] >= time_start and  candle['t'] <= time_stop:
            candle['t']=str(datetime.datetime.fromtimestamp(ms/1000.0))
            candles_9_to_16.append(candle)


    df = pd.read_json(json.dumps(candles_9_to_16))
    df = df.set_index(pd.DatetimeIndex(df['t']))
    df = df.drop(['t'], axis=1)
    df = df.drop(['vw'], axis=1)
    df = df.drop(['n'], axis=1)

    df = df.rename(columns={'o': 'open', 'c': 'close',   'h': 'high', 'v': 'volume', 'l': 'low'   } , index={'t': 'datetime'})

    df = df.reindex(columns=['open',"high","low","close","volume"])
    #print(df)
    return df
