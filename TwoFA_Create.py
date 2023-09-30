# from twilio.rest import Client
# import json
#
# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# client = Client(account_sid, auth_token)
#
# new_factor = client.verify \
#                    .v2 \
#                    .services('VA965c3b543caed3dc59019d53c7f0725b') \
#                    .entities('ff483d1ff591898a9942916050d2ca3f') \
#                    .new_factors \
#                    .create(
#                         friendly_name="TestAccount1",
#                         factor_type='totp'
#                     )
#
# print(new_factor.sid)
# print(new_factor.entity_sid)
# print(new_factor.binding)

from twilio.rest import Client
import os

#UUID should be without hyphens
def Create2FAFactor(UUID, account_name):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    new_factor = client.verify \
                   .v2 \
                   .services('VA965c3b543caed3dc59019d53c7f0725b') \
                   .entities(UUID) \
                   .new_factors \
                   .create(
                        friendly_name=account_name,
                        factor_type='totp'
                    )
    return new_factor #pass it on and use uri from new_factor.binding to generate a QR code for the user
