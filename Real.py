import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from Pause import *
from Emailer import *
from time import sleep

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
stopping = 0




def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('I am listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    again = ('Please say the command again.')
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'hello' in command:
        talk('Hello there')
    elif 'email number one' in command:
        talk('Sending...')
        emailSender(1)
        talk('Sent!')
    elif 'email number 2' in command:
        talk('Sending...')
        emailSender(2)
        talk('Sent!')
    elif 'email number two' in command:
        talk('Sending...')
        emailSender(2)
        talk('Sent!')
    elif 'email number three' in command:
        talk('Sending...')
        emailSender(3)
        talk('Sent!')
    elif 'email number for' in command:
        talk('Sending...')
        emailSender(4)
        talk('Sent!')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'start hot potato' in command:
        talk('Lets play!')
        pywhatkit.playonyt('Najbolje dečije pesme - Pet malih majmuna, Kad si srećan i druge | Pesme za decu')
        sleep(5)
        pauza()
    elif 'stop stop stop' in command:
        stopping = 1
    else:
        talk(again)
        print(again)

while stopping == 0:
    run_alexa()