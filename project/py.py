import requests

r = requests.get('https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1')

print(r.text)

#https://www.youtube.com/watch?v=KgAtZ1LlNiQ
