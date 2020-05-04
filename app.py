import requests
import json
import time
from twilio.rest import Client
from time import sleep


def reptcode():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "d0f71ba5a0mshf4b880875940051p1b89bbjsnbe090d81a1d4"
        }
    
    response = requests.request("GET", url, headers=headers)
    
    x=response.json()
    data= json.dumps(x['state_wise']['Uttar Pradesh']['district']['Agra'],indent=1)
    agra_data=json.loads(data)
    conf_cases=agra_data['confirmed']
    recovered_cases=agra_data['recovered']
    deaths=agra_data['deceased']
    
    
    account_sid='ACa08ab12086fd09d24847dcc70d5cf09f'
    auth_token='bc7e641c0d6b063ccc7fb3d8c70b7e5a'
    
    
    client = Client(account_sid, auth_token)
    
    localtime=time.localtime()
    result=time.strftime("%I:%M:%S %p", localtime)
    
    
    c1=conf_cases
    r1=recovered_cases
    phno=['+918077787160','+919719100779','+919719600779','+919760789998']
    for i in phno:
        bod='\n\n\n As of time {} today \nTotal cases in Agra are {} and recovered cases are {} plus the no.of deaths are {}'.format(result,c1,r1,deaths)
        message = client.messages \
            .create(
                body=bod,
                from_='+12057514198',
                to=i )
        print(message.sid)

if __name__ == '__main__':        
	reptcode()
