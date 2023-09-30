

##############################################
#copied from twilio docs, feel free to remove#
##############################################

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#
# from twilio.rest import Client
# import os
# account_sid = os.environ['TWILIO_ACCOUNT_SID'] #set env variables to twilio account sid
# auth_token = os.environ['TWILIO_AUTH_TOKEN'] #set env variables to twilio account auth token
# client = Client(account_sid, auth_token)
# factor = client.verify.v2 \
#                       .services('VA965c3b543caed3dc59019d53c7f0725b') \
#                       .entities('40a9227edff04c599a037ee5fa5e8000') \
#                       .factors('YF02651873b333bb5d1453b6e4e85181ed') \
#                       .update(auth_payload='442596')
# #
# print(factor.status)

from twilio.rest import Client
import os

def Verify2FAFactorCreation(UUID, factor_sid, auth_code):
    account_sid = os.environ['TWILIO_ACCOUNT_SID'] #set env variables to twilio account sid
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] #set env variables to twilio account auth token
    client = Client(account_sid, auth_token)
    factor_result = client.verify \
                   .v2 \
                   .services('VA965c3b543caed3dc59019d53c7f0725b') \
                   .entities(UUID) \
                   .factors(factor_sid) \
                   .update(auth_payload=auth_code)
    return factor_result.status #can return the whole factor, but we only need to see whether verification succeeded or not
