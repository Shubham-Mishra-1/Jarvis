import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#Change voice
engine.setProperty('voice',voices[1].id)
#Speak Fn
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening sir")
    speak("I am friday, I am Here To Help You, What You Want Me To Do.")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query
if __name__ == '__main__':
    wishme()
    while True:
        query=takeCommand().lower()

        #logics
        if 'wikipedia' in query:
            speak('Searching on wikipedia....')
            query =query.replace('wikipedia','')
            results= wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # famous apps
        elif 'youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'open insta' in query:
            webbrowser.open('instagram.com')
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        elif 'open whatsapp' in query:
            webbrowser.open('whatsapp.com')
        elif 'open map' in query:
            webbrowser.open('Googlemaps.com')
        elif 'open gethub' in query:
            webbrowser.open('gethub.com')
        elif 'open amazon' in query:
            webbrowser.open('amazon.in')
        elif 'open flipkart' in query:
            webbrowser.open('flipkart.in')
        elif 'open zomato' in query:
            webbrowser.open('zomato.in')
        elif 'open uber' in query:
            webbrowser.open('uber.in')
        elif 'open google classroom' in query:
            webbrowser.open('https://classroom.google.com/u/2/h')

        #Youtube Channel
        elif 'flying beast' in query:
            webbrowser.open('https://www.youtube.com/results?search_query=flyingbeast')
        elif 'tech burner' in query:
            webbrowser.open('https://www.youtube.com/channel/UCXUJJNoP1QupwsYIWFXmsZg')
        elif 'rom rom ji' in query:
            webbrowser.open('https://www.youtube.com/channel/UCzOVIHSg-GeenFlGHttWQwA')
        elif 'shroud' in query:
            webbrowser.open('https://www.youtube.com/channel/UCoz3Kpu5lv-ALhR4h9bDvcw')
        elif 'carryminati' in query:
            webbrowser.open('https://www.youtube.com/user/AddictedA1')
        elif 'JerryRigEverything' in query:
            webbrowser.open('https://www.youtube.com/user/JerryRigEverything')
        elif 'Unbox Therapy' in query:
            webbrowser.open('https://www.youtube.com/user/unboxtherapy')
        elif 'mortal' in query:
            webbrowser.open('https://www.youtube.com/channel/UC7Q7pl0z0MrdayvmAnchlJQ')

        #elif 'play music' in query:
            #music_dir='here write your path'
            #songs=os.listdir(music_dir)
            #os.startfile(os.path.join(music_dir,song[ramndom.random.randint(1,10)]))

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'its {strTime}')
        elif 'day' in query:
            strTime=datetime.datetime.now().day
            speak(f'its {strTime}')
        elif 'open steam' in query:
            codepath="C:\\Program Files (x86)\\Steam\\Steam.exe"
            os.startfile(codepath)
        elif 'open valorant' in query:
            codepath="C:\\Riot Games\\VALORANT\\Riot Client\\RiotClientServices.exe"
            os.startfile(codepath)
        elif 'open c plus plus' in query:
            codepath="C:\Program Files (x86)\Dev-Cpp\devcpp.exe"
            os.startfile(codepath)
        elif 'open SQL' in query:
            codepath="C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" "--defaults-file=C:\ProgramData\MySQL\MySQL Server 8.0\my.ini" "-uroot" "-p"
            os.startfile(codepath)
        elif 'open getting over it' in query:
            codepath="C:\movies\Getting Over It with Bennett Foddy [Pc Games]\GettingOverIt.exe"
            os.startfile(codepath)


