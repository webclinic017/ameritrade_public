
def search_for_last_trend(candles,comparation, index):
   

    for previous in range(index, 0,-1):
        if "tendencia" in candles["candle_type"][previous]:
            if comparation in candles["candle_type"][previous]:
                return True
            else:
                return False
    return False

            