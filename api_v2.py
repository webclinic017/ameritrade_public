from flask import Flask, render_template
import pandas as pd 
from datetime import datetime, timedelta
# import to avoid errors of threads 
import matplotlib.pyplot as mpl
mpl.switch_backend('agg')



import mplfinance as mpf 
from threading import Thread
import queue

from get_price_history import get_price_history 
from classify_candles import classify_candles
from get_hammers import get_hammers
from get_gap import get_gap
from get_max_and_min import get_max_and_min 
from graph_max_and_min import graph_max_and_min
from table_type_actions import table_type_actions
from max_and_min_comparison import max_and_min_comparasion
from check_trend import check_trend
from check_lateral_trend import check_lateral_trend
from search_for_roof_and_floor import search_for_roof_and_floor
from get_action_call import get_action_call
from get_action_put import get_action_put
from get_real_time_data import get_real_time_data
from send_report import send_report
from stop_conditions import stop_conditions
from get_price_history_poligon import get_price_history_poligon





app = Flask(__name__)

def create_graph(symbol,period, periodType,frecuencyType,frecuency,cola, low_rank, high_rank):
    pd.options.mode.chained_assignment = None
    img= "static/assets/img/{}.png".format(symbol)
    title= "{} prices (Last {} days)".format(symbol,period)
    
    
    #candles = get_price_history(symbol=symbol, period=period, periodType=periodType, frecuencyType=frecuencyType, frecuency=frecuency)
    today = datetime.today()
    ten_days_ago = today - timedelta(days=15)
    ten_days_ago = datetime.strftime(ten_days_ago, '%Y-%m-%d')
    one_day_ago = today - timedelta(days=1)
    one_day_ago = datetime.strftime(one_day_ago, '%Y-%m-%d')
    today = datetime.strftime(today, '%Y-%m-%d')
    candles = get_price_history_poligon(symbol=symbol, multiplier="60", timespan="minute",from_date=ten_days_ago,to_date=one_day_ago)
    
    print(ten_days_ago)
    print("_____________________________________________ 15 days ago ____________________________________________________________")
    try:
        time_now = datetime.now()
        if time_now.hour >= 9:
            candles_real_time = get_real_time_data(symbol=symbol, multiplier="60", timespan="minute",from_date=today,to_date=today)
            candles = candles.append(candles_real_time)
    except:
        print("dia no laboral")
    #pd.set_option('display.max_rows', candles.shape[0]+1)
    
    #print(candles)

    candles = classify_candles(candles)
    candles = get_hammers(candles)
    candles= get_gap(candles)
    candles = get_max_and_min(candles)
    max, min = graph_max_and_min(candles)
    candles = max_and_min_comparasion(candles)
    candles =check_trend(candles)
    candles = check_lateral_trend(candles)
    candles = search_for_roof_and_floor(candles)


    





    candles = get_action_call(candles)
    candles = get_action_put(candles)
    send_report(candles, symbol, low_rank, high_rank)
    stop_conditions(candles,symbol)
    

    table_type_actions(candles, cola)
    apds = [
         mpf.make_addplot(max,type='scatter',markersize=10,color='r',marker='^'),
         mpf.make_addplot(min,type='scatter',markersize=10,color='g',marker='v'),
       ]

    mpf.plot(candles,addplot=apds, type='candle', title=title , style='charles',savefig=img)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/apple')
def apple():
    img= "static/assets/img/AAPL.png"
    cola = queue.LifoQueue()


    create_graph_thread = Thread(target=create_graph, args=("AAPL",10,'day','minute','30',cola, 0, .80))
    create_graph_thread.start()
    data  =cola.get()
    return render_template('apple.html', img=img, data=data)

@app.route('/amazon')
def amazon():
    img= "static/assets/img/AMZN.png"
    cola = queue.LifoQueue()
    create_graph_thread = Thread(target=create_graph, args=("AMZN",10,'day','minute','30',cola, 0,5))
    create_graph_thread.start()
    data  =cola.get()
    return render_template('amazon.html',  img=img, data=data)

@app.route('/bank_of_america')
def bank_of_america():
    img= "static/assets/img/BAC.png"
    cola = queue.LifoQueue()
    create_graph_thread = Thread(target=create_graph, args=("BAC",10,'day','minute','30',cola,0,.1))
    create_graph_thread.start()
    data  =cola.get()
    return render_template('bank_of_america.html', img=img, data=data)

@app.route('/facebook')
def facebook():
    img= "static/assets/img/FB.png"
    cola = queue.LifoQueue()
    create_graph_thread = Thread(target=create_graph, args=("FB",10,'day','minute','30',cola,0,.80))
    create_graph_thread.start()
    data  =cola.get()
    return render_template('facebook.html', img=img, data=data)



@app.route('/moderna')
def moderna():
    img= "static/assets/img/MRNA.png"
    cola = queue.LifoQueue()
    create_graph_thread = Thread(target=create_graph, args=("MRNA",10,'day','minute','30',cola,0,5))
    create_graph_thread.start()
    data =cola.get()
    return render_template('moderna.html',  img=img, data=data)


    



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)




