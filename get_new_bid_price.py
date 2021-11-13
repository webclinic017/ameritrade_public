

import requests 

from dotenv import load_dotenv
import os
load_dotenv(".env")




from find_next_friday import find_next_friday

def get_new_bid_price(**kwargs):


    key = os.environ["API_KEY_AMERITRADE"]
    params = {}
    params.update({'apikey':key})
    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)

    url ="https://api.tdameritrade.com/v1/marketdata/chains?apikey={}&symbol={}&contractType={}&toDate={}".format(
        
        params['apikey'],
        params['symbol'],
        params['contractType'],
        params['toDate']

    )
    response =requests.get(url).json()






    if params['contractType'] == "CALL":
        contract_type = "callExpDateMap"
    elif params['contractType'] == "PUT":
        contract_type = "putExpDateMap"


 
    for expiration_date_data in response[contract_type]:
        for data in response[contract_type][expiration_date_data]:
            if data == params["strike"]:
                for contract in response[contract_type][expiration_date_data][data]:
                    return  contract["bid"]


if __name__ == "__main__":
    
    print(type(get_new_bid_price(symbol="AAPL", contractType="CALL", toDate=find_next_friday(), strike ="205.0" )))

