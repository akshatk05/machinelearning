import speech_recognition as sr
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import winspeech
bot = ChatBot('test')
conv = open('conv.txt','r').readlines()
bot.set_trainer(ListTrainer)
bot.train(conv)
def talk(t):
 for i in  range(t):
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    y = r.recognize_google(audio) 
  response = bot.get_response(y)
  winspeech.say (response)
def text(t):
 for i in range(t):
  bot = ChatBot('test')
  conv = open('conv.txt','r').readlines()
  bot.set_trainer(ListTrainer)
  bot.train(conv)
  x =  input("you: ")
  response = bot.get_response(x)
  print (response)