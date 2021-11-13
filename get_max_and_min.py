
import pandas as pd 


'cambiar el numero de resta de  velas y quitar el dia cuando sea tiempo real '

def get_max_and_min(candles):
    
    
    for  index  in range(2,len(candles['open'])):
        
        if candles.index[index].hour  == 10 and candles.index[index].minute ==0  :

            if "gap al alza" in candles['candle_type'][index-1]:
                if 'bajista' in  candles['candle_type'][index] and 'alcista' in  candles['candle_type'][index-1] :
                    if  candles['close'][index] <= candles['open'][index-1] : 
                        candles['candle_type'][index - 1]   = 'maximo '  + candles['candle_type'][index -1]


            elif 'bajista' in  candles['candle_type'][index] and 'alcista' in  candles['candle_type'][index-1] :
                if "hammer" in  candles['candle_type'][index -1]:
                    if  candles['close'][index] <= candles['open'][index-1] : 
                        candles['candle_type'][index - 1]   = 'maximo '  + candles['candle_type'][index -1]
                elif candles['close'][index] <= candles['open'][index-1] : 
                    candles['candle_type'][index - 1]   = 'maximo '  + candles['candle_type'][index -1]
                
                



        
        if 'bajista' in  candles['candle_type'][index]   and   'alcista' in  candles['candle_type'][index -1]    and  'alcista' in   candles['candle_type'][index -2 ]   :
        #if 'hammer' not in candles['candle_type'][index -1]:
            candles['candle_type'][index - 1]   = 'maximo '  + candles['candle_type'][index -1] 

        elif  'alcista' in   candles['candle_type'][index]  and  'bajista' in candles['candle_type'][index -1]     and  'bajista' in  candles['candle_type'][index -2 ]   :
        #if 'hammer' not in candles['candle_type'][index -1] :
            candles['candle_type'][index - 1]   = 'minimo '  + candles['candle_type'][index -1]


        #condicion de minimo recientemente agregada 
        """
        if  'bajista' in   candles['candle_type'][index]  and  'alcista' in candles['candle_type'][index -1]     and  'bajista' in  candles['candle_type'][index -2 ]   :
            if candles['close'][index] >= candles['close'][index -2]:
                candles['candle_type'][index - 1]   = 'minimo '  + candles['candle_type'][index -2]
        """
         
    pd.set_option('display.max_rows', candles.shape[0]+1)
    #print(candles)
    return candles



    