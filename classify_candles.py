import pandas as pd 


def classify_candles(candles):
    # candles["candle_type"] = [""] * candles.shape[0]
    candles['candle_type'] = ''
    
    for index in range(len(candles['open'])):

        if candles['open'][index] > candles['close'][index]:
            candles['candle_type'][index] = 'bajista'

        elif candles['open'][index] < candles['close'][index]:
            candles['candle_type'][index] = 'alcista'
        elif candles['open'][index] == candles['close'][index]:
            candles['candle_type'][index] = 'doji'

    pd.set_option('display.max_rows', candles.shape[0]+1)
    # print(candles)
    return candles
