import os
import time
import pyttsx3
from datetime import datetime
import pytz

tts = pyttsx3.init()
intro = "Hello. I'm Jarvis, your virtual assistant. Type help for a list of commands to try me out."
response = ""
unread=""
suitact=False
opendoor=False
isflying=False
Charged=True
Battery="100%"

print("+------+")
print("|JARVIS|")
print("+------+\n\n")
print(intro)

tts.say(intro)
tts.runAndWait()


def Executecmd(command):
  if command == "help" or command == "h": 
    response="Here's a list of basic commands. For a complete list of all my commands, type: commands.\n\n"
    unread="Time: tells you the time (also works with 'time in Spain')\nSuit: activates or deactivates Ironman's suit\nOpen: opens the Avenger's Building's door\nFly: makes you fly while you have the suit on\nCharge: charges Ironman's suit\nBattery: tells you the suits current battery"
  elif command == "hello" or command == "hi":
    response="Um... hi."
    unread=""
  elif command == "suit" or command == "activate suit":
    global suitact
    
    if suitact == False:
      suitact=True
      response="Suit activated"
      unread=""
    else:
      suitact=False
      response="Suit deactivated"
      unread=""
  elif command == "time in spain" or command == "time":
    tz_SP = pytz.timezone('Europe/Madrid') 
    datetime_SP = datetime.now(tz_SP)
    response="This is the time in Spain: "
    unread=datetime_SP.strftime("%H:%M:%S")
  else: 
    response="Sorry, i didn't understand that command."
    unread=""
  
  print(response + unread)
  tts.say(response)
  tts.runAndWait()


while True:
  response = str(input("\n"))
  cmd = response.lower()
  
  print("\n")
  Executecmd(cmd)







  
