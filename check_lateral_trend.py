import pandas as pd 
from check_condition_for_trend import check_condition_for_trend
from search_for_last_trend import search_for_last_trend


def check_lateral_trend(candles):
    for index in range(1, len(candles['open'])):
        if 'MIN ALCISTA' in candles['candle_type'][index]:
            condition_1_case_1 = check_condition_for_trend(candles, "MIN ALCISTA", index, 1)

            if condition_1_case_1: 
                for previous in range(index-1, 0, -1):
                    if "MAX" in candles['candle_type'][previous]:
                        if "MAX BAJISTA" in candles['candle_type'][previous]:
                            condition_2 = check_condition_for_trend(candles, "MAX ALCISTA", previous, 0)
                            if condition_2:
                                if not search_for_last_trend(candles, "lateral", index):
                                    candles['candle_type'][index] = 'tendencia lateral 1 ' + candles['candle_type'][index]
                                    break
                                else: 
                                    break
                        else:
                            break

        elif 'MAX BAJISTA' in candles['candle_type'][index]:
            condition_1_case_2 = check_condition_for_trend(candles, "MAX BAJISTA", index, 0)
            
            if condition_1_case_2: 
                for previous in range(index-1, 0, -1):
                    if "MIN" in candles['candle_type'][previous]:
                        if "MIN ALCISTA" in candles['candle_type'][previous]:
                            condition_2 = check_condition_for_trend(candles, "MIN BAJISTA", previous, 1)
                            if condition_2:
                                if not search_for_last_trend(candles, "lateral", index):
                                    candles['candle_type'][index] = 'tendencia lateral 2 ' + candles['candle_type'][index]
                                    break
                                else:
                                    break
                        else:
                            break

    pd.set_option('display.max_rows', candles.shape[0]+1)
    # print(candles)
    return candles
