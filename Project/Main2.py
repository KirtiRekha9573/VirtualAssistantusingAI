# 1st Step: Writing a Speak function. Give an argument as audio. The Virtual Assistant will pronounce the audio
#Install pyttsx3 module. Using Microsoft speech API called as sapi5 to take and use inbuilt voices from windows

import pyttsx3
import speech_recognition as sr
#import pyaudio
import Main
import datetime
import shutil
import ctypes
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

#def username():
    #speak("What should I call you Sir")
    #uname = takeCommand()
    #speak("Welcome Mister")
    #speak(uname)

    #columns = shutil.get_terminal_size().columns
     
    #print("#####################".center(columns))
    #print("Welcome Mr.", uname.center(columns))
    #print("#####################".center(columns))

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
    #username()
    #speak("Hello Kirti")
    #Writing the while loop
    while True:
        #Converting the query into the lower string
        query = takeCommand().lower()
        #Logic for executing tasks based on query

        #Coding for opening applications
        if 'open visual studio code' in query:
           code_path = "C:\\Users\\CSUFTitan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
           os.startfile(code_path)

        elif 'open outlook' in query:
            outlook_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Outlook"
            os.startfile(outlook_path)

        elif 'open command prompt' in query:
            cmd_path = "C:\\WINDOWS\\system32\\cmd"
            os.startfile(cmd_path)

        #For changing the background
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\CSUFTitan\\Pictures\\wallpaper2.jpg", 0)
            speak("Background changed successfully")

        #For writing a note
        elif "write a note" in query:
            speak("What should I write, Sir")
            note = takeCommand()
            file = open('C:\\Users\\CSUFTitan\\Documents\\Spring SEM(Last)\\VirtualAssistantusingAI\\ProjectKirti.txt', 'w')
            speak("Sir, should I include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note) 

        elif "show note" in query:
            speak("Showing Notes")
            file = open("Kirti.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "execute java program" in query:
            speak("Which program you want to execute?")
            program_name = takeCommand()
            file = 'C:\\Users\\CSUFTitan\\Documents\\Spring SEM(Last)\\VirtualAssistantusingAI\\Project\\' + program_name
            print("javac " + program_name)
            break
            speak("Press Enter")

        elif "execute python program" in query:
            speak("Which program you want to execute?")
            #print("Which program you want to execute?")
            python_name = takeCommand()
            file_path = 'C:\\Users\\CSUFTitan\\Documents\\Spring SEM(Last)\\VirtualAssistantusingAI\\Project\\' +  python_name
            print(python_name)
            speak("You have entered" +  python_name)
            speak("Go ahead")
            break
            speak("Press Enter")
            
        #Coding for exiting the program
        elif 'exit' in query:
            exit
            speak("Okay Bye")
            break

        
