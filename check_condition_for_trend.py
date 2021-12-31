def check_condition_for_trend(candles, comparation, index, operator):
    max_or_min = ""
    if "MIN" in comparation:
        max_or_min = "MIN"
    elif "MAX" in comparation:
        max_or_min = "MAX"

    for previous in range(index-1, 0, -1):
        if max_or_min in candles["candle_type"][previous]:
            if comparation in candles["candle_type"][previous]:
                if operator == 1:
                    if candles['close'][index] > candles['close'][previous]:
                        return True
                    else:
                        return False 
                if operator == 0:
                    if candles['close'][index] < candles['close'][previous]:
                        return True
                    else: 
                        return False

            else: 
                return False
