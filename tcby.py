import requests

response = requests.get('https://www.facebook.com/tcbyoflenoir')


if "dairy free" in response.text:
    #send sms
    print ("found it")
else:
    print("didn't find it")