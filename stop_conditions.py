from database import ask_purchases, update_status_of_actions
from send_email import send_email_multiple_contracts
from datetime import datetime, timedelta
from find_next_friday import find_next_friday
from get_new_bid_price import get_new_bid_price
from dotenv import load_dotenv
import os
load_dotenv(".env")


def stop_conditions(candles,symbol):
    EMAIL = os.environ["EMAIL"]
    time_now = datetime.now()
    inferior_time_limit = time_now - timedelta(minutes= 65)
    superior_time_limit = time_now + timedelta(minutes= 65)
    list_of_contracts = []
    for  index  in range(2,len(candles['open'])):
        if candles.index[index] > inferior_time_limit and candles.index[index] < superior_time_limit:

            if "bajista" in candles['candle_type'][index]:
                if candles['close'][index] < candles['open'][index -2 ]:
                    list_of_purchases = ask_purchases(status= "on posession", symbol=symbol, call_or_put ="call")
                    list_of_purchases_updated=[]
                    if len(list_of_purchases) > 0:
                        candles['action_type'][index] = ' stop action call condition 1 ' + candles['action_type'][index]

                        for purchase in list_of_purchases :
                            new_bid_price = get_new_bid_price(symbol=symbol, contractType="CALL", toDate=find_next_friday(), strike =str(purchase[3]) )
                            if new_bid_price != None:
                                print("hacemos el update call condition 1")

                                update_status_of_actions(new_bid_price,purchase[6])
                                list_of_purchases_updated.append((purchase[0],purchase[1],purchase[2],purchase[3],purchase[4],new_bid_price))

                            

                        subject = "stop action call condition 1"
                        send_email_multiple_contracts(EMAIL ,subject ,list_of_purchases_updated)
                        send_email_multiple_contracts("eydmax0@gmail.com" , subject , list_of_purchases_updated)




            if "alcista" in candles['candle_type'][index]:
                if candles['close'][index] > candles['open'][index -2 ]:
                    list_of_purchases = ask_purchases(status= "on posession", symbol=symbol, call_or_put ="put")
                    list_of_purchases_updated=[]
                    if len(list_of_purchases) > 0:
                        candles['action_type'][index] = ' stop action put condition 1 ' + candles['action_type'][index]

                        for purchase in list_of_purchases :
                            new_bid_price = get_new_bid_price(symbol=symbol, contractType="PUT", toDate=find_next_friday(), strike =str(purchase[3]) )
                            if new_bid_price != None:
                                print("hacemos el update put condition 1")

                                update_status_of_actions(new_bid_price,purchase[6])
                                list_of_purchases_updated.append((purchase[0],purchase[1],purchase[2],purchase[3],purchase[4],new_bid_price))


                        subject = "stop action put condition 1"
                        send_email_multiple_contracts(EMAIL ,subject ,list_of_purchases_updated)
                        send_email_multiple_contracts("eydmax0@gmail.com" , subject , list_of_purchases_updated)

                        
