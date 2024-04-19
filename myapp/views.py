from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from .quotes import getQoute
from .jokes import getJokes
from dotenv import load_dotenv
import os

@csrf_exempt
def home(request):
    load_dotenv()
    account_sid = os.environ.get("ACCOUNT_SID")
    print(account_sid)
    auth_token = os.environ.get("AUTH_TOKEN")
    twillio_number = os.environ.get("TWILIO_NUMBER")
    client = Client(account_sid,auth_token)
    if request.method == "POST":
        message = request.POST
        user_name =message["ProfileName"]
        user_number  = message["From"]
        user_message =message["Body"]
        print(user_message)
        if user_message.lower() in ["hie","hello","hi","hey","hy"]:
            client.messages.create(
                from_ = f"whatsapp: {twillio_number}",
                body=f"Hie {user_name}",
                to=user_number
            )
        elif "quote" in user_message.lower():
            #quote love
            category = user_message[5:].strip()
            user_quote =getQoute(category)
            if isinstance(user_quote,str):
                 client.messages.create(
                from_=f"whatsapp:{twillio_number}",
                body=user_quote,
                to = user_number )
            else:
                current_quote = user_quote[0]['quote']
                current_author = user_quote[0]['author']
                client.messages.create(
                    from_=f"whatsapp:{twillio_number}",
                    body=f"QOUTE: {current_quote}\nAUTHOR: {current_author}",
                    to = user_number )
        elif "joke" in user_message.lower():
            #logic for the other api
            joke = getJokes()
            current_joke = joke[0].get("joke")
            client.messages.create(
                    from_=f"whatsapp:{twillio_number}",
                    body=f"JOKE:{current_joke}",
                    to = user_number )

        else:
            client.messages.create(
                from_=f"whatsapp{twillio_number}",
                body="Am only trained to respond to English greetings and fetch random qoutes and weather based on location",
                to=user_number
            )



        
    return render(request,"home.html")