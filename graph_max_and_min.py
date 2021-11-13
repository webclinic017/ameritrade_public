import numpy as np



def graph_max_and_min(candles):
    min =[]
    max=[]
    
    
    for  index  in range(len(candles['open'])):
        if 'maximo' in candles['candle_type'][index]:
            max.append(candles['close'][index] +.2 )
            min.append(np.nan)
        elif 'minimo' in candles['candle_type'][index]:
            min.append(candles['close'][index] -.2 )
            max.append(np.nan)
        else: 
            max.append(np.nan)
            min.append(np.nan)
    
    

    return max, min 

