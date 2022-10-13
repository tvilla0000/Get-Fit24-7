from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC198cac608257418645e13b9dcc9b3189"
# Your Auth Token from twilio.com/console
auth_token  = "85500aa7aa071e7c1e62660231b014a2"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19253502272", 
    from_="+19706717118",
    body="Hello from Python!")

print(message.sid)