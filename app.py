import requests
import json
import time
from twilio.rest import Client
from time import sleep
import api_covid
import api_twilio
from api_twilio import auth_token,account_sid
from api_covid import head



def accquire_location():
    global state
    state=input('Enter your state name: (Ex-Uttar Pradesh):')
    global city
    city=input('Enter your city name: (Agra):')

def get_user_phone_number():
    global phno
    phno=[]
    ele=int(input("Enter no of phone numbers you want to feed:"))
    for i in (0,ele)
        inp=str(input("Enter only the verified number by twilio:"))
        phno.append(inp)

def get_twilio_number():
    global my_phno
    my_phno=str(input("Enter Phone number Provided by twilio account:"))

def reptcode():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
    
    response = requests.request("GET", url, headers=head)
    
    x=response.json()
    data= json.dumps(x['state_wise'][state]['district'][city],indent=1)
    agra_data=json.loads(data)
    conf_cases=agra_data['confirmed']
    recovered_cases=agra_data['recovered']
    deaths=agra_data['deceased']
    
    
    client = Client(account_sid, auth_token)
    
    localtime=time.localtime()
    result=time.strftime("%I:%M:%S %p", localtime)
    
    
    c1=conf_cases
    r1=recovered_cases
    
    for i in phno:
        bod='\n\n\n As of time {} today \nTotal cases in {},{} are {} and recovered cases are {} plus the no.of deaths are {}'.format(result,city,state,c1,r1,deaths)
        message = client.messages \
            .create(
                body=bod,
                from_=my_phno,
                to=i )
        print(message.sid)

if __name__ == '__main__':        
	reptcode()
