import matplotlib.pyplot as plt
from textblob import TextBlob
import winspeech
import numpy as np
import speech_recognition as sr
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
print ("if you need help just type in help") 
def listing(n):
 p = []
 for x in range(n):
  p = p + [x]
 y = x + 1
 p = p + [y]
 p.remove(0)
 return (p)
def sentdex():
 x = 0
 text = input("what do you want to sentdex ") 
 blob = TextBlob(text)

 words = blob.words
 
 words_len = len(words)

 p = []

 for i in range(words_len):
  word = words[x]
  h = TextBlob(word)
  hsenti = h.sentiment.polarity
  hsenti = (hsenti * 10) + 2
  p = p + [hsenti]
  x = x + 1
 words_len = listing(words_len)
 plt.plot(words_len,p)

 plt.show()

def  translate(lang):
 text = input("what do you want to translate ")
 blob = TextBlob(text)
 if lang == 'en':
  winspeech.say(text)
 abc = blob.translate(to=lang)
 winspeech.say(abc)
 print (abc)
 return (abc)
def tags():
 text = input("what do you want to find parts of speech ") 
 blob = TextBlob(text)
 print (blob.tags)
 return (blob.tags)
def spell_check():
 b = input("whats do you want to correct ")
 b = TextBlob(b)
 print (b.correct())

def sentiment():
 text = input("what do you want the sentiment of")
 b = TextBlob(text)
 c = b.sentiment.polarity
 if c > 0:
  print ("sentiment = positive")
  return ("positive")
 if c < 0:
  print ("sentiment = negative")
  return ("negative")
def say():
 x = input("waddya wanna say")
 winspeech.say(x)
def help():
 print ("oh so i see that you are having some trouble with my library here and you know what im here to help")
 print ("heres a small introduction on the library")
 print ("--------------------------------------------")
 print ("intro")
 print ("nlp or natural language proccessing is my library built on top of textblob (make sure you have it installed before installing this)")
 print ("--------------------------------------------")
 print ("heres the list of functions and what they can do")
 print ("1.sentdex: my personal favorite however describing what it does will take a while but i promise you it will be worthwhile once your done")
 print ("when you speak with someone / anyone whenever happy or sad words are used these words cause fluctuations in the feeling of the conversation")
 print ("what if we could map these fluctuations well do i have a finction for you. you just feed what you want to say to sentdex ")
 print ("2.listing: it just amkes a list till the number (eg. listing(5) = [1,2,3,4,5]")
 print ("3.translate:it translates anything into a host of languages heres a list of the languges (en,es)")
 print ("4.tags: this gives you the parts of speech tags")
 print ("5.sentiment:this gives you the sentiment(emotion of the text)")
 print ("6.spell_check: checks and corrects spelling")
 print ("7.say: it says what you give it")
 print ("8.hear: it will hear and print what it hears")
 print ("9.chatbot(x): no nlp library is complete without its own chatbot feed it x and it feeds you a response")
 print ("tokenization: tokenize words or sentances")
 print ("this is akshat(the author of this library) signing off")

def hear():
 r = sr.Recognizer()
 with sr.Microphone() as source:
  print("Say something!")
  audio = r.listen(source)
  y = r.recognize_google(audio)
 print (y)
 return(y)

def chatbot(x):
 bot = ChatBot('test')
 conv = open('conv.txt','r').readlines()
 bot.set_trainer(ListTrainer)
 bot.train(conv)
 response = bot.get_response(x)
 print (response)
 return (response)

def tokenize():
 t = input("do you want to tokenize to sentances or words[s/w]")
 if t == 's':
  c = input("what do you what to tokenize")
  c = TextBlob(c)
  p = c.sentances
  print (p)
  return (p)
 elif t == 'w':
  c = input("what do you what to tokenize")
  c = TextBlob(c)
  p = c.words
  print (p)
  return (p)