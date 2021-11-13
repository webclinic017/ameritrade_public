import smtplib
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv(".env")


def send_email(send_to,subject, messages):
    send_from = os.environ["EMAIL"]
    password = os.environ["EMAIL_PASSWORD"]
    text_message =""
    for key,value in messages.items() :
        text_message += str(key)+ ": " +str(value)  + "\n"
    
    email_text = """
    \From: {}
    To: {}
    Subject: {}

    {}
    """.format(send_from, send_to, subject, text_message)
    print(email_text)
    try:
        mailServer = smtplib.SMTP('smtp.gmail.com',587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(send_from, password)
        mailServer.sendmail(send_from, send_to, email_text)
        mailServer.close()
    except :
        print ("Error: unable to send email")




def send_email_multiple_contracts(send_to,subject, messages):
    send_from = os.environ["EMAIL"]
    password = os.environ["EMAIL_PASSWORD"]
    text_message =""
    for message  in messages :
        text_message += "symbol: "+ str(message[0]) +", action_type: " + str(message[1]) +", candle_date: " + str(message[2]) +", strike: " + str(message[3]) + ", ask_price: " + str(message[4]) + ", bid_price: "  + str(message[5]) + ", time of request: "+str(datetime.now()) + "\n"
    
    email_text = """
    \From: {}
    To: {}
    Subject: {}

    {}
    """.format(send_from, send_to, subject, text_message)
    print(email_text)
    try:
        mailServer = smtplib.SMTP('smtp.gmail.com',587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(send_from, password)
        mailServer.sendmail(send_from, send_to, email_text)
        mailServer.close()
    except :
        print ("Error: unable to send email")




