import pandas as pd 



def search_for_roof_and_floor(candles):
    
    
    for  index  in range(1,len(candles['open'])):
        
        
        if 'tendencia lateral' in  candles['candle_type'][index]: 
                for previous_max in range(index-1, 0,-1):
                    if "MAX" in  candles['candle_type'][previous_max]:
                        candles['candle_type'][previous_max]   = 'techo '  + candles['candle_type'][previous_max]
                        break
                for previous_min in range(index-1, 0,-1):
                    if "MIN" in  candles['candle_type'][previous_min]:
                        candles['candle_type'][previous_min]   = 'piso '  + candles['candle_type'][previous_min]
                        break
                                





            


    pd.set_option('display.max_rows', candles.shape[0]+1)
    #print(candles)
    return candles