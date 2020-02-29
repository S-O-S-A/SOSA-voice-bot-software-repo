import ddg3
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC97c3b2c95124846c016aee609b362807"
# Your Auth Token from twilio.com/console
auth_token = "aeb32d9efcfc58dfe862b512d15a8a9b"
client = Client(account_sid, auth_token)

def textPrompt(info):
    choice = input("Would you like me to text you this information? Enter 1 or 0")
    if(choice == '1'):
        message = client.messages.create(
        to="4192979382", 
        from_="5203946350",
        body= "Hey, its S.O.S.A with your search info: " + info)

searchQuery = input()

r = ddg3.query(searchQuery)
print(r.type)


if(r.type == 'disambiguation'):
    print("Here are the first couple results related to what you said:")
    
    print(r.related[0].text)
    info = "\n" + r.related[0].text
    print(r.related[1].text)
    info = "\n" + r.related[1].text
    textPrompt(info)


elif(r.type == 'answer'):
    print(r.abstract.text)
    info = "\n" + r.abstract.text
    textPrompt(info)
elif(r.type == 'nothing'):
    print("Here are some results related to your search:")
    print(r.related)
    info = "\n" + r.related
    textPrompt(info)

