import pandas as pd 
from datetime import datetime
from  search_for_last_max_or_min import search_for_last_max_or_min
from search_for_last_trend import search_for_last_trend



def get_action_call(candles):
    candles['action_type'] =''




    'cambiar el numero de resta de  velas y quitar el dia cuando sea tiempo real '
    
    for  index  in range(1,len(candles['open'])):
        
        now = datetime.now()
        today_9_candle = now.replace(hour=9, minute=0, second=0, microsecond=0)
        today_1059_candle = now.replace(hour=10, minute=59, second=0, microsecond=0)







        if candles.index[index] == today_1059_candle:
            if  "MIN" in candles['candle_type'][index]:
                if "bajista" in candles['candle_type'][index -2] and "alcista" in candles['candle_type'][index -1]:
                        if search_for_last_trend(candles, "al alza", index):
                            candles['action_type'][index] = "call condition 1"
                                


                elif  "gap a la baja" in candles['candle_type'][index -2] and "alcista" in candles['candle_type'][index -2]:
                    if "alcista" in candles['candle_type'][index -1]:
                        if search_for_last_trend(candles, "al alza", index):
                            candles['action_type'][index] = "call condition 2"
                               

            elif "alcista" in candles['candle_type'][index]:
                if "alcista" in candles['candle_type'][index -1]:
                    if "bajista" in candles['candle_type'][index -2 ] and "gap al alza" in candles['candle_type'][index -2]:
                        if search_for_last_max_or_min(candles, "MIN", index):
                            if search_for_last_trend(candles, "al alza", index):
                                candles['action_type'][index] = "call condition 7"
                                   





        
            
                                 

        if    candles.index[index]   > today_9_candle:                     
            if "alcista" in candles['candle_type'][index]  and "bajista" in candles['candle_type'][index-1]:
                if candles["close"][index] > candles["open"][index -1 ] :
                    if search_for_last_max_or_min(candles, "MIN", index):
                        if search_for_last_trend(candles, "al alza", index):
                            candles['action_type'][index] = "call condition 4"
                            
                elif candles["close"][index] > candles["open"][index -1 ]:
                    if search_for_last_trend(candles, "al alza", index):
                        
                        candles['action_type'][index] = "call condition 6"


            if "hammer" in candles["candle_type"][index]:
                if   "inverse"  not in candles["candle_type"][index]:
                    if "bajista" in candles["candle_type"][index-1]:
                        if search_for_last_max_or_min(candles, "MIN", index):
                            if search_for_last_trend(candles, "al alza", index):
                                for previous in range(index, 0,-1):
                                    if  candles.index[previous]   ==today_930_candle:
                                        if "alcista" in candles["candle_type"][previous]:
                                            candles['action_type'][index] = "call condition 3"


            if "alcista" in candles["candle_type"][index]:
                for previous in range(index, 0,-1):
                    if "tendencia" in candles["candle_type"][previous]:
                        if "lateral" in candles["candle_type"][previous]:
                            for previous_2 in range(previous,0,-1):
                                if "techo" in candles["candle_type"][previous_2]:
                                    #aqui deberia ser comparacion con el piso 
                                    if candles["close"][index] > candles["high"][previous_2]:
                                        count_call_condition = 0
                                        count_lateral_trend = 0
                                        for register in range(index, 0,-1):
                                            if candles['action_type'][register] == "call condition 8":
                                                count_call_condition += 1 
                                            if "tendencia lateral" in  candles['candle_type'][register]:
                                                count_lateral_trend += 1
                                        if count_call_condition <count_lateral_trend:
                                            candles['action_type'][index] = "call condition 8"
                                            break
                                    else: 
                                        break
                        else:
                            break
                              


            elif "MIN" in candles['candle_type'][index]:
                if search_for_last_trend(candles, "al alza", index):
                    candles['action_type'][index] = "call condition 5"
                            

            


        



        


   
    pd.set_option('display.max_rows', candles.shape[0]+1)
    #print(candles)
    return candles


