from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()
# Your Account SID from twilio.com/console
def send_error_login():
    account_sid = os.getenv("accountSID")
    # Your Auth Token from twilio.com/console
    auth_token  = os.getenv("authToken")

    client = Client(account_sid, auth_token)

    personal = "+9779843552060"

    message = client.messages.create(
        to= f"{personal}",
        from_="+18149626993",
        body="Failed Login in the Secret project")

    print(message.sid)
