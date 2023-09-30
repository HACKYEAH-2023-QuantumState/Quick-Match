import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def GetFactor(UUID):
    factor = client.verify.v2 \
                       .services('VA965c3b543caed3dc59019d53c7f0725b') \
                       .entities(UUID) \
                       .fetch()
    return factor

