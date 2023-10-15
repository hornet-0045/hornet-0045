import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init(driverName='espeak')
voices= engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning!")

    elif hour>=12 and hour<=18:
        speak("good afternoon!")

    else:
        speak("good evening!")
    speak("I am jarvis sir, plese tell me  how can i assist you")     

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listning.....")
        r.pause_threshold = 1
        r.energy_threshold=300
        r.adjust_for_ambient_noise(source,duration=1)
       
        audio = r.listen(source)

    try:
       print("recognizing")
       query=r.recognize_google(audio,language='en-in')
       print(f"user said: {query}")
    except Exception as e:
        print(e)

        print("say that again please")
    
        return "None"
    return query
if __name__=="__main__":
   wishMe()

   while True:
        query=takecommand().lower()


        if 'wikipedia' in query:
           speak("searching wikipedia")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("accroding to wikipedia")
           print(results)
           speak(results)
       
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S") 
            speak(strTime)    

