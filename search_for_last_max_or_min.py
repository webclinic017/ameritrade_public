def search_for_last_max_or_min(candles,comparation, index):
   

    for previous in range(index, 0,-1):
        if "MAX" in candles["candle_type"][previous] or "MIN" in candles["candle_type"][previous] :
            if comparation in candles["candle_type"][previous]:
                return True
            else:
                return False 
    return False
            