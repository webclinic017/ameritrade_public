from run_automatic_request import run_automatic_request
from database import ask_purchases, update_status_of_actions
from send_email import send_email_multiple_contracts
from datetime import datetime

#run_automatic_request()

#list_of_purchases = ask_purchases(status= "selled", symbol="FB", call_or_put ="put")
#subject = "stop action put condition 3"
#send_email_multiple_contracts("jglg191995@gmail.com" ,subject ,list_of_purchases)


#update_status_of_actions(111,38)
print(datetime.now())