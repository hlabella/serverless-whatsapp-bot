from twilio.rest import Client
import os

def send_whatsapp_message(event, context):

    # Twilio credentials from environment variables
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    from_whatsapp_number = 'whatsapp:' + os.environ['FROM_WHATSAPP_NUMBER']
    to_whatsapp_number = 'whatsapp:' + os.environ['TO_WHATSAPP_NUMBER']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body='Hello Coutinho',
                              from_=from_whatsapp_number,
                              to=to_whatsapp_number
                          )

    print(message.sid)
