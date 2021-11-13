from datetime import datetime
import pandas as pd 

'cambiar el numero de resta de  velas y quitar el dia cuando sea tiempo real '

def get_gap(candles):
    
    
    for  index  in range(len(candles['open'])):
        
        now = datetime.now()
        today_9_candle = now.replace(hour=9, minute=0, second=0, microsecond=0)

        if candles.index[index]   == today_9_candle:
            if candles['open'][index]  > candles['close'][index -1]:
                candles['candle_type'][index] = 'gap  al alza '  + candles['candle_type'][index] 
            elif  candles['open'][index]  < candles['close'][index -1]:
                candles['candle_type'][index] = 'gap  a la baja '  + candles['candle_type'][index] 

    pd.set_option('display.max_rows', candles.shape[0]+1)
    #print(candles)
    return candles



