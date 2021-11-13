


import pandas as pd 



def max_and_min_comparasion(candles):
    
    
    for  index  in range(1,len(candles['open'])):
        
        
        if 'maximo' in  candles['candle_type'][index]:
            for previous in range(index -1,0,-1):

                if 'maximo' in  candles['candle_type'][previous]:

                    if candles['close'][index] > candles['close'][previous]:
                        candles['candle_type'][index]   = 'MAX ALCISTA '  + candles['candle_type'][index]
                    elif candles['close'][index] < candles['close'][previous]:
                        candles['candle_type'][index]   = 'MAX BAJISTA '  + candles['candle_type'][index]
                    break
        if 'minimo' in  candles['candle_type'][index]:
            for previous in range(index -1,0,-1):
                if 'minimo' in  candles['candle_type'][previous]:

                    if candles['close'][index] > candles['close'][previous]:
                        candles['candle_type'][index]   = 'MIN ALCISTA '  + candles['candle_type'][index]
                    elif candles['close'][index] < candles['close'][previous]:
                        candles['candle_type'][index]   = 'MIN BAJISTA '  + candles['candle_type'][index]
                    break 




    pd.set_option('display.max_rows', candles.shape[0]+1)
    #print(candles)
    return candles
