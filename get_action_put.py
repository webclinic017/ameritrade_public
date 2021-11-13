import pandas as pd 
from datetime import datetime
from  search_for_last_max_or_min import search_for_last_max_or_min
from search_for_last_trend import search_for_last_trend



def get_action_put(candles):
  




    'cambiar el numero de resta de  velas y quitar el dia cuando sea tiempo real '
    
    for  index  in range(1,len(candles['open'])):
        
        now = datetime.now()
        today_9_candle = now.replace(hour=9, minute=0, second=0, microsecond=0)
        today_1059_candle = now.replace(hour=10, minute=59, second=0, microsecond=0)
        




        if candles.index[index]   == today_1059_candle:
            if "bajista" in candles['candle_type'][index-1]:
                if search_for_last_max_or_min(candles,"MAX",index-1):
                    if "gap a la baja" in candles['candle_type'][index -1]:
                        candles['action_type'][index] = "put condition 1"


            if "gap al alza" in candles['candle_type'][index -1] and  "bajista" in candles['candle_type'][index-1]:
                if search_for_last_max_or_min(candles,"MAX",index):
                    candles['action_type'][index] = "put condition 6"

            if "gap al alza" in candles['candle_type'][index -1] and  "inverse hammer" in candles['candle_type'][index-1]:
                if "bajista" in candles['candle_type'][index] and "alcista" in candles['candle_type'][index -1]:
                    if candles["close"][index] < candles["open"][index -1 ]: 
                        candles['action_type'][index] = "put condition 6.2"
            

            


        if candles.index[index] > today_9_candle:
            if "bajista" in candles['candle_type'][index] and  "alcista" in candles['candle_type'][index-1]:
                if candles["close"][index] < candles["open"][index -1]:
                    if search_for_last_max_or_min(candles,"MAX",index):
                        if search_for_last_trend(candles,"a la baja",index):
                            candles['action_type'][index] = "put condition 2"

            if "bajista" in candles["candle_type"][index]:
                for previous in range(index, 0,-1):
                    if "tendencia" in candles["candle_type"][previous]:
                        if "lateral" in candles["candle_type"][previous]:
                            for previous_2 in range(previous,0,-1):
                                if "piso" in candles["candle_type"][previous_2]:
                                    #aqui deberia ser comparacion con el piso 
                                    if candles["close"][index] < candles["low"][previous_2]:
                                        count_call_condition = 0
                                        count_lateral_trend = 0
                                        for register in range(index, 0,-1):
                                            if candles['action_type'][register] == "put condition 7":
                                                count_call_condition += 1 
                                            if "tendencia lateral" in  candles['candle_type'][register]:
                                                count_lateral_trend += 1
                                        if count_call_condition <count_lateral_trend:
                                            candles['action_type'][index] = "put condition 7"
                                            break

                                    else: 
                                        break
                        else:
                            break
            
            if "inverse hammer" in candles['candle_type'][index-1]  and "bajista" in candles['candle_type'][index] :
                if search_for_last_max_or_min(candles,"MAX",index):
                        candles['action_type'][index] = "put condition 3"

            if "bajista" in candles['candle_type'][index] and  "inverse hammer" in candles['candle_type'][index-1]:
                if search_for_last_max_or_min(candles,"MAX",index):
                    if search_for_last_trend(candles,"a la baja",index):
                        candles['action_type'][index] = "put condition 4"
            
            if "bajista" in candles["candle_type"][index]:
                if search_for_last_max_or_min(candles,"MIN ALCISTA",index):
                    for previous in range(index,0,-1):
                        if "MIN AlCISTA" in candles["candle_type"][previous]:
                            if candles["close"][index] < candles["close"][previous]:
                                if search_for_last_trend(candles,"al alza",index):
                                    candles['action_type'][index] = "put condition 5"



        


   
    pd.set_option('display.max_rows', candles.shape[0]+1)
    print(candles)
    return candles


