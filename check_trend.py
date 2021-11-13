import pandas as pd 
from check_condition_for_trend import check_condition_for_trend


def check_trend(candles):
    
    
    for  index  in range(1,len(candles['open'])):
        
        
        if 'MIN ALCISTA' in  candles['candle_type'][index]:
            condition_1_case_1 = check_condition_for_trend(candles,"MIN ALCISTA", index,1)
            condition_1_case_2_and_3 = check_condition_for_trend(candles,"MIN BAJISTA", index,1)
           

            if condition_1_case_1: 
                for previous in range(index-1, 0,-1):
                    if "MAX" in  candles['candle_type'][previous]:
                        if "MAX ALCISTA" in  candles['candle_type'][previous]:
                            condition_2  =  check_condition_for_trend(candles,"MAX ALCISTA", previous,1)
                            if condition_2:
                                candles['candle_type'][index]   = 'tendencia al alza '  + candles['candle_type'][index]
                                break
                        else:
                            break
                                
            elif condition_1_case_2_and_3: 
                for previous in range(index-1, 0,-1):
                    if "MAX" in  candles['candle_type'][previous]:
                        if "MAX ALCISTA" in  candles['candle_type'][previous]:
                            condition_2  =  check_condition_for_trend(candles,"MAX ALCISTA", previous,1)
                            condition_3  =  check_condition_for_trend(candles,"MAX BAJISTA", previous,1)
                            if condition_2:
                                candles['candle_type'][index]   = 'tendencia al alza '  + candles['candle_type'][index]
                                break
                            elif condition_3:
                                 candles['candle_type'][index]   = 'tendencia al alza '  + candles['candle_type'][index]
                                 break
                        
                        else:
                            break





        elif  'MAX BAJISTA' in  candles['candle_type'][index]:
            condition_1_case_4 = check_condition_for_trend(candles,"MAX BAJISTA", index,0)
            condition_1_case_6 = check_condition_for_trend(candles,"MAX ALCISTA", index,0)
            condition_1_case_7 = check_condition_for_trend(candles, "MAX ALCISTA", index,0)
            if condition_1_case_4: 
                for previous in range(index-1, 0,-1):
                    if "MIN" in  candles['candle_type'][previous]:
                        if "MIN BAJISTA" in  candles['candle_type'][previous]:
                            condition_2  =  check_condition_for_trend(candles,"MIN BAJISTA", previous,0)
                            if condition_2:
                                candles['candle_type'][index]   = 'tendencia a la baja '  + candles['candle_type'][index]
                                break
                        else:
                            break

            elif condition_1_case_6:
                
                for previous in range(index-1, 0,-1):
                    if "MIN" in  candles['candle_type'][previous]:
                        if "MIN ALCISTA" in  candles['candle_type'][previous]:
                           
                            condition_2  =  check_condition_for_trend(candles,"MIN ALCISTA", previous,1)
                            if condition_2:
                                candles['candle_type'][index]   = 'tendencia a la baja '  + candles['candle_type'][index]
                                break
                        else:
                            break
            if condition_1_case_7:
                candles['candle_type'][index]   = 'tendencia a la baja '  + candles['candle_type'][index]

                



        elif  'MIN ALCISTA' in  candles['candle_type'][index]:
            condition_1_case_5 = check_condition_for_trend(candles,"MAX BAJISTA", index,1)
            if condition_1_case_5: 
                for previous in range(index-1, 0,-1):
                    if "MIN" in  candles['candle_type'][previous]:
                        if "MIN BAJISTA" in  candles['candle_type'][previous]:
                            condition_2  =  check_condition_for_trend(candles,"MAX BAJISTA", previous,0)
                            if condition_2:
                                candles['candle_type'][index]   = 'tendencia a la baja '  + candles['candle_type'][index]
                                break
                        else:
                            break


    pd.set_option('display.max_rows', candles.shape[0]+1)
    #print(candles)
    return candles
