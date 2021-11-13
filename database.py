
# pip3 install mysqlclient
import MySQLdb
from datetime import datetime

from dotenv import load_dotenv
import os
load_dotenv(".env")

DB_HOST = os.environ["DB_HOST_SQL"]
DB_USER = os.environ["DB_USER_SQL"]
DB_NAME = os.environ["DB_NAME_SQL"]
DB_PASS = os.environ["DB_PASS_SQL"]




#connection string 
data = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 

#connecting 
conn = MySQLdb.connect(*data) 

# crate a cursor to execute querys 
cursor = conn.cursor()


def insert_data(symbol,
candle_date, open_value,
close_value,action_type,
call_or_put,strike,
ask_price,bid_price,
status_of_action,
order_date):
	#connecting
	conn = MySQLdb.connect(*data)
	# crate a cursor to execute querys
	cursor = conn.cursor()
	query = ("insert into  register_of_call_and_put_actions" 
	"(symbol, candle_date, open_value, close_value, action_type,"
	"call_or_put, strike, ask_price, bid_price, status_of_action, order_date)"
	"values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" 
	)
	values = (str(symbol) ,
	str(candle_date) ,
	str(open_value) ,
	str(close_value) ,
	str(action_type) ,
	str(call_or_put),
	str(strike) ,
	str(ask_price),
	str(bid_price),
	str(status_of_action) ,str(order_date)
	)
	#print(query)
	cursor.execute(query, values)
	# commit the changes and close connection
	cursor.close()
	conn.commit()
	conn.close()  



def ask_purchases(status,symbol, call_or_put):
	list_of_purchases = []
	#connecting
	conn = MySQLdb.connect(*data)
	# crate a cursor to execute querys
	cursor = conn.cursor()
	query = ("select symbol, action_type, candle_date, strike ,ask_price ,bid_price,id from  register_of_call_and_put_actions where status_of_action = %s and  symbol = %s and call_or_put = %s"  )
	#print(query)
	values = (status,symbol, call_or_put)
	cursor.execute(query,values)
	records = cursor.fetchall()
	for record in records:
		print(record)
		list_of_purchases.append(record)

	cursor.close()
	conn.close() 
	return list_of_purchases


def update_status_of_actions(strike, id ):
	#connecting
	conn = MySQLdb.connect(*data)
	# crate a cursor to execute querys
	cursor = conn.cursor()
	query = ("update register_of_call_and_put_actions set status_of_action='selled', strike=%s where id=%s")
	#print(query)
	values = (strike,id)
	cursor.execute(query,values)

	conn.commit()
	cursor.close()
	conn.close()

if __name__ == '__main__':
	insert_data(symbol= "AAPL",
	candle_date="2021-10-04 09:30:00", 
	open_value= 1.1,
	close_value=2.2,
	action_type="put condition 1",
	call_or_put= "put",
	strike=3.3,
	ask_price=4.4,
	bid_price=5.5,
	status_of_action="on posession",
	order_date=datetime.now())
	
	ask_purchases(status= "on posession", symbol="AAPL", call_or_put="call")
