

import requests 
import datetime

import pytz
from dotenv import load_dotenv
import os
load_dotenv(".env")




def test_market_options(**kwargs):

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

    list_of_contracts = []

    dict_of_contract = {
        "strike":"",
        "ask":"",
        "bid":"",
        "expiration_date":""    
    }


    if params['contractType'] == "CALL":
        contract_type = "callExpDateMap"
    elif params['contractType'] == "PUT":
        contract_type = "putExpDateMap"


    tz_new_york = pytz.timezone("America/New_York") 
    for expiration_date_data in response[contract_type]:
        for data in response[contract_type][expiration_date_data]:
            for contract in response[contract_type][expiration_date_data][data]:
                ms = contract['expirationDate']
                expiration_date=datetime.datetime.fromtimestamp(ms/1000.0, tz_new_york)

                if contract["ask"] >= params['low_rank'] and contract["ask"] <= params['high_rank'] :
                    list_of_contracts.append((data, contract['ask'], contract["bid"] ,str(expiration_date)))


    ask_prices = []
    if len(list_of_contracts) >0:
        for contract in list_of_contracts:
            ask_prices.append(contract[1])
        
        max_value_ask = max(ask_prices)

        max_value_ask_index = ask_prices.index(max_value_ask)
        dict_of_contract["strike"] =list_of_contracts[max_value_ask_index][0] 
        dict_of_contract["ask"] =list_of_contracts[max_value_ask_index][1]
        dict_of_contract["bid"] = list_of_contracts[max_value_ask_index][2]
        dict_of_contract["expiration_date"] =list_of_contracts[max_value_ask_index][3]
        print (dict_of_contract)
        return dict_of_contract

    return None

    




