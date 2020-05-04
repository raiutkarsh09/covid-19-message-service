from time import sleep
import app

...
print('Before using this make sure you\'ve entered api details' )

choice=str(input("Do you wish to setup?: y/n"))

if(choice=='y'):
    app.get_twilio_number()
    app.accquire_location()
    choice=str(input("Do you wish to Enter user phone numbers?: y/n"))
    if(choice=='y'):
        app.get_user_phone_number()
    elif(choice=='n'):
        break

elif(choice=='n'):
    break
    

if __name__ == '__main__':
    while True:
        sleep(25200) # sleeps for 5 seconds
        app.reptcode()
