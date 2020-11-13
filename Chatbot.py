'''
Date: 11/12/2020
Project: Chatbot
Author: Pranav Khiste

'''

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime, date


bot = ChatBot('Buddy', storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello',
'How are you',
'I am good, Thank you!',
'What is your mobile number',
'You can reach at me on +1(617)-309-6090',
'Can I have your email ID?',
'Sure. Its khiste.p@northeastern.edu ',
'Where do you live',
'Boston !!',
'What do you do',
'I am a Data Scientist / Data Engineer, currently pursuing masters degree in Information systems at Northeastern University.',
'where are you from',
'India',
'fuck off',
'Pardon me ',
'Okay Thanks',
'No Problem! Have a Good Day!'
])


name=input("Enter Your Name: ")

now = datetime.now()
today = now.strftime("%A")
time= now.strftime("%H:%M:%S")

print("Hi, I am Bot!!")
print(f"Today is {today}, current time is {time} ")
print("Let me know how can I help you?")

while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)