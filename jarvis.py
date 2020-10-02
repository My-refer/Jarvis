import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('good morning')
    elif hour <= 0 and hour >=12:
        speak('good afternoon')
    else:
        speak("good evening")
    speak("I am jarvis sir, Please tell me how may I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 0.5 
        
        audio = r.listen(source=source, timeout=5, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query} \n ")
    except Exception as e:
        print(e) # it prints the error
        print("Say that again please...")
        return"None"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('umairiqbal9889@gmail.com', 'Salman44!!!!')
    server.sendmail('umairiqbal9889@gmail.com',to,content)
    server.close()
    
    
    



if __name__=="__main__":
    wishMe()
    while True:
    #if 1:
        query = takecommand().lower()
        
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 1 )
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
            
        elif "open google" in query:
            webbrowser.open("google.com")
            
        elif "search youtube" in query:
            speak("What should I search in youtube?")
            youtubeQuery = takeCommand()
            webbrowser.open("www.youtube.com/results?search_query=" + youtubeQuery)
            
        elif "search google" in query:
            speak("What should I search in google?")
            searchQuery = takeCommand()
            webbrowser.open("www.google.com/results?search_query=" + searchQuery)
            
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            
        elif "play music" in query:
            music_dir = "E:\\The Polar Express (2004)[Dual Audio]\\asma"
            songs = os.listdir(music_dir)
            #print(songs)
            a = random.randint(1,147)
            os.startfile(os.path.join(music_dir, songs[a]))
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
            
        elif "open code " in query:
            codePath = "C:\\Users\\Umair Iqbal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif "email to me" in query:
            try:
                speak('what do you want to speak')
                content = takecommand()
                to = "umairiqbal9889@gmail.com"
                sendmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send this email...")
                
        elif "thank you bye" in query:
            speak("You are welcome Sir")
            break
