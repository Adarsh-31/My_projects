from twilio.rest import TwilioRestClient
account_sid = "AC95f8184bcc85ae83adb049f792f7835e"
auth_token = "ea2c76d5979dbeaa3be41f1697e4cbd8"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "do you know payal",
    to = "+917610339953",
    from_ = "+16698004019")

print (message.sid)