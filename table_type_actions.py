

def table_type_actions(candles, cola):
    data = []
    item = {}
    for  index  in range(len(candles['open'])):
        item = {
            'date': str(candles.index[index]),
            'type_of_candle': candles['candle_type'][index],
            'action':  candles['action_type'][index]
        }
        data.append(item)

    cola.put(data)
