# Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client
#

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# client = Client(account_sid, auth_token)
#
# import os
# from twilio.rest import Client
#
# challenge = client.verify \
#                   .v2 \
#                   .services('VA965c3b543caed3dc59019d53c7f0725b') \
#                   .entities('ff483d1ff591898a9942916050d2ca3f') \
#                   .challenges \
#                   .create(
#                        auth_payload='820806',
#                        factor_sid='YF0265185129b84b2a01cb45e9942fd9f4'
#                    )
#
# print(challenge.status)

from twilio.rest import Client
import os

def Validate2FA(UUID, target_factor_sid, auth_code):
    
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    challenge = client.verify \
                  .v2 \
                  .services('VA965c3b543caed3dc59019d53c7f0725b') \
                  .entities(UUID) \
                  .challenges \
                  .create(
                       auth_payload=auth_code,
                       factor_sid=target_factor_sid
                   )
    return challenge.status #can return whole challenge, but status is probably enough

