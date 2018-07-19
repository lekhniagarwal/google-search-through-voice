
# it takes input from microphone and then convert it to text and then play it and make google url and using web scraping take url of first link and then open the first link

import speech_recognition as sr

import webbrowser as wb
import speak # speak.py is file
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import time, os



chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!') # say play despacito
    audio = r.listen(source)
    print ('Done!')
try:
    text = r.recognize_google(audio)
    print('Google thinks you said:\n' + text)
    lang = 'en'

    speak.tts(text, lang)

    f_text = 'https://www.google.co.in/search?q=' + text
    r = requests.get(f_text)

    soup = BeautifulSoup(r.text, "html.parser")

    #print (soup.find('cite').text)  #it will get the first link 
   
    wb.get(chrome_path).open(soup.find('cite').text) #open the first link



except Exception as e:
    print (e)


for item in soup.findAll('cite'):
    print (item.text)

print("ok\n")

for item in soup.select(".r a"):
    print (item.get_text())