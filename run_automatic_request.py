import requests
import time 
from datetime import datetime
from database import ask_purchases, update_status_of_actions
from dotenv import load_dotenv
import os
load_dotenv(".env")

def run_automatic_request():
    url = 'http://127.0.0.1:8000/apple'
    print("request to apple")
    response =requests.get(url)
    time.sleep(20)

    url = 'http://127.0.0.1:8000/amazon'
    print("request to amazon")
    response =requests.get(url)
    time.sleep(20)

    url = 'http://127.0.0.1:8000/bank_of_america'
    print("request to bank of america")
    response =requests.get(url)
    time.sleep(20)
    
    url = 'http://127.0.0.1:8000/facebook'
    print("request to facebook")
    response =requests.get(url)
    time.sleep(20)

    url = 'http://127.0.0.1:8000/moderna'
    print("request to moderna")
    response =requests.get(url)
    time.sleep(20)






if __name__ == "__main__":
    EMAIL = os.environ["EMAIL"]
    while True:
        today = datetime.today()
        
        if today.hour == 9 and today.minute == 59:
            run_automatic_request()
            time.sleep(40)
    
        if today.hour == 10 and today.minute == 59:
            run_automatic_request()
            time.sleep(40)

        if today.hour == 11 and today.minute == 59:
            run_automatic_request()
            time.sleep(40)

        if today.hour == 12 and today.minute == 59:
            run_automatic_request()
            time.sleep(40)

        if today.hour == 13 and today.minute == 59:
            run_automatic_request()
            time.sleep(40)

        if today.hour == 14 and today.minute == 59:
            run_automatic_request()
            time.sleep(40)

        if today.hour == 15 and today.minute == 58:
            run_automatic_request()
            time.sleep(40)

        today = datetime.today()
        if today.isoweekday() == 5:
            if today.hour == 15 and today.minute == 58:
                list_of_symbols =["AAPL","AMZN","BAC", "FB", "MRNA"]
                for symbol in list_of_symbols:
                    list_of_purchases = ask_purchases(status= "on posession", symbol=symbol, call_or_put ="call")
                    list_of_purchases_updated = []
                    if len(list_of_purchases) > 0:
                        candles['action_type'][index] = ' stop action call condition 3 ' + candles['action_type'][index]


                        print(list_of_purchases)
                        for purchase in list_of_purchases :
                            new_bid_price = get_new_bid_price(symbol=symbol, contractType="CALL", toDate=find_next_friday(), strike =str(purchase[3]) )
                            if new_bid_price != None:
                                print("hacemos el update call condition 3")

                                update_status_of_actions(new_bid_price,purchase[6])
                                list_of_purchases_updated.append((purchase[0],purchase[1],purchase[2],purchase[3],purchase[4],new_bid_price))

                            

                        print(list_of_purchases_updated)
                        subject = "stop action call condition 2"
                        send_email_multiple_contracts(EMAIL ,subject ,list_of_purchases_updated)
                        send_email_multiple_contracts("eydmax0@gmail.com" , subject , list_of_purchases_updated)




                    list_of_purchases = ask_purchases(status= "on posession", symbol=symbol, call_or_put ="put")
                    list_of_purchases_updated
                    if len(list_of_purchases) > 0:
                        candles['action_type'][index] = ' stop action put condition 3 ' + candles['action_type'][index]


                        for purchase in list_of_purchases :
                            new_bid_price = get_new_bid_price(symbol=symbol, contractType="PUT", toDate=find_next_friday(), strike =str(purchase[3]) )
                            if new_bid_price != None:
                                print("hacemos el update put condition 2")

                                update_status_of_actions(new_bid_price,purchase[6])
                                list_of_purchases_updated.append((purchase[0],purchase[1],purchase[2],purchase[3],purchase[4],new_bid_price))

                            


                        subject = "stop action put condition 3"
                        send_email_multiple_contracts(EMAIL ,subject ,list_of_purchases_updated)
                        send_email_multiple_contracts("eydmax0@gmail.com" , subject , list_of_purchases_updated)






                time.sleep(40)
        

