# Covid-19 District-wise Messaging service

This Project informs user and their added phone numbers ever 7 hours about the Current Status of COVID-19 patients in their district.
It is based on collecting and sending data using REST APIs


It uses REST APIs like [Twilio-messaging-api](https://www.twilio.com/) and [covid-19-tracker RapidAPI](https://rapidapi.com/spamakashrajtech/api/corona-virus-world-and-india-data/)



### API's To Be Used
* [Twilio-messaging-api](https://www.twilio.com/)
* [Covid-19-tracker RapidAPI](https://rapidapi.com/spamakashrajtech/api/corona-virus-world-and-india-data/)

##### Before Installation make youre you have got the authoization token an client id from both the APIs
###

### Installation

This project requires python3 enviorment installed on your system.
First collect the api keys from twilio and create a virtual phone number.
Suscribe to the Covid-19-tracker Rapid API and view endpoints.

##### To setup the api keys open the api_covid.py and api_twilio.py and fill the respective fields

Install the requirements:

```sh
$ cd covid_19_message_service
$ pip install -r requirements.txt
```
To finish setting up open terminal in same folder and wirte:
```sh
$ python3 run.py &
```




