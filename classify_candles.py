import pandas as pd 


def classify_candles(candles):
    #candles["candle_type"] = [""] * candles.shape[0]
    candles['candle_type'] =''
    
    for  index  in range(len(candles['open'])):
     


        if  candles['open'][index] > candles['close'][index]:
            candles['candle_type'][index] = 'bajista'
            #print ("open: {} ,close: {}  type: {} ".format(candles['open'][index], candles['close'][index], candles['candle_type'][index]))
        elif candles['open'][index] < candles['close'][index]:
            candles['candle_type'][index] = 'alcista'
        elif candles['open'][index] == candles['close'][index]:
            candles['candle_type'][index] = 'doji'
        
            #print ("open: {} ,close: {}  type: {} ".format(candles['open'][index], candles['close'][index], candles['candle_type'][index]))
    
    pd.set_option('display.max_rows', candles.shape[0]+1)
    #print(candles)
    return candles
