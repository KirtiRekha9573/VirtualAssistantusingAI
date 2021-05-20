# 1st Step: Writing a Speak function. Give an argument as audio. The Virtual Assistant will pronounce the audio
#Install pyttsx3 module. Using Microsoft speech API called as sapi5 to take and use inbuilt voices from windows

import pyttsx3
import speech_recognition as sr
#import pyaudio
import datetime
import shutil
import feedparser
import ctypes
import wikipedia
import webbrowser
import os
import re
import smtplib
import pyjokes
import json
from urllib.request import urlopen
import wolframalpha
import requests
import csv
import time
import subprocess
import tkinter
from selenium import webdriver


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
#setting the voice for the engine
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Writing a wish function according to the current time using speak function.
#We have typecasted hour into integer. It can give us the hour in 24 hours format.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    assname = ("Kirti 1.0")
    speak("I am your virtual assistant Sir! Please tell me how may I help you?")

def username():
    speak("What should I call you Sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)

    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        speak("Say that again please")
        #None is returning the string, if any problem comes
        return "None"
    return query

#Writing the main method and calling speak function and wishMe function too#
if __name__ == "__main__":
    clear = lambda: os.system('cls')
    wishMe()
    username()
    #speak("Hello Kirti")
    #Writing the while loop
    while True:
        #Converting the query into the lower string
        query = takeCommand().lower()
        #Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open wikipedia' in query:
            webbrowser.open("https://www.wikipedia.org/")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        #Coding for opening gmail
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        #Playing Songs/Videos
        elif 'play music' in query:
            music_dir = 'C:\\Users\\CSUFTitan\\Pictures\\Songs'
            #With the help of os module, we are going to list the music
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        #Coding for knowing the time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        
        #Normal Conversation
        elif 'how are you' in query:
            speak("I am fine. Thank you")
            print("I am fine. Thank you")
            speak("How are you")

        elif 'fine' in query or 'good' in query:
            speak("It is good to know that you are fine")
            print("It is good to know that you are fine")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Kirti")
            print("I have been created by Kirti")

        elif "who i am" in query:
            speak("If you talk then definately you are a human")
            print("If you talk then definately you are a human")

        elif 'why you came to this world' in query:
            speak("Thanks to Kirti...Further, it is a secret")
            print("Thanks to Kirti...Further, it is a secret")
        
        #For telling a joke
        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        #Coding for knowing the news
        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f4f2f2252f414c3285f28eabc0d74130")
                data = json.load(jsonObj)
                i = 1

                speak("Here are some top news")
                print('------------ US NEWS -----------'+ '\n')

                for item in data['articles']:
                    print(str(i)+ '. '+item['title']+'\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        #For calculations
        elif "calculate" in query:
            app_id = "Q3HGW2-X9EJKWXGR6"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("Q3HGW2-X9EJKWXGR6")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        #For system related commands
        elif "lock window" in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "shut down the system" in query:
            speak("Your system on its way to shut down")
            subprocess.call('shutdown /p / f')

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want assistant to stop listening")
            a = int(takeCommand())
            time.speech(a)
            print(a) 
        #Coding for exiting the program
        elif 'exit' in query:
            exit
            speak("Okay Bye")
            break