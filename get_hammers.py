import pandas as pd 


def get_hammers(candles):
    
    for  index  in range(2,len(candles['open'])):
        hammer_condition_1 = (candles['high'][index] - candles['low'][index]) > 3*(candles['open'][index] - candles['close'][index])
        hammer_condition_2 =  (( candles['close'][index] - candles['low'][index])/(candles['high'][index] - candles['low'][index]) > 0.6)
        hammer_condition_3 = ((candles['open'][index] - candles['low'][index])/(candles['high'][index] - candles['low'][index]) > 0.6)

        # valor default 0.6
        hammer_inverse_condition_1 = (candles['high'][index] - candles['low'][index])>3*(candles['open'][index] -candles['close'][index]) 
        hammer_inverse_condition_2 =  ((candles['high'][index] - candles['close'][index])/(candles['high'][index] - candles['low'][index]) > 0.6) 
        hammer_inverse_condition_3 = ((candles['high'][index] - candles['open'][index])/(candles['high'][index] - candles['low'][index]) > 0.6)





        if 'alcista' in candles['candle_type'][index] and   hammer_condition_1 and  hammer_condition_2 and hammer_condition_3 :
            candles['candle_type'][index] = 'hammer ' + candles['candle_type'][index] 

        elif   'bajista' in candles['candle_type'][index] and  hammer_condition_1 and  hammer_condition_2 and hammer_condition_3 :
            candles['candle_type'][index] = 'hammer ' + candles['candle_type'][index] 


        elif  'alcista' in candles['candle_type'][index] and   hammer_inverse_condition_1 and  hammer_inverse_condition_2 and hammer_inverse_condition_3 :
            candles['candle_type'][index] = ' inverse hammer '  + candles['candle_type'][index] 



        elif  'bajista' in candles['candle_type'][index] and   hammer_inverse_condition_1 and  hammer_inverse_condition_2 and hammer_inverse_condition_3 :
            candles['candle_type'][index] = ' inverse hammer ' + candles['candle_type'][index] 
    
    pd.set_option('display.max_rows', candles.shape[0]+1)
    #print(candles)
    return candles