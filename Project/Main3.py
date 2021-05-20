import speech_recognition as sr
import smtplib
import webbrowser
import time
import pyttsx3
r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('Sorry, say that again please')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

#For sending an email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    #Enable low security in gmail
    server.login('kirtichaudhari070495@gmail.com', 'KirtiC@95')
    server.sendmail('kirtichaudhari070495@gmail.com', to, content)
    server.close()

def respond(voice_data):
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for' + search)

    if 'find location' in voice_data:
        location = record_audio('What location you would like to search?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        print(location)
        webbrowser.get().open(url)
        print('Here is the location of ' + location)

    if 'email to Sam' in voice_data:
        try:
            print("What should I say?")
            content = record_audio()
            to = "krchaudharib4u@gmail.com"
            sendEmail(to, content)
            print("Email has been sent..!")
        except Exception as e:
            print(e)
            print("I am not able to send this email")


time.sleep(1)
print('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data) 
    if 'exit' in voice_data:
        exit
        print("Okay Bye")
        break
       


    
    