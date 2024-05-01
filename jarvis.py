import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. tell me your command ")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
    
        #logic for executing tasks
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Sameeksha S Kotian\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open vscode' in query:
            codePath = "C:\\Users\\Sameeksha S Kotian\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open notepad' in query:
            codePath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'open cmd' in query:
            codePath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(codePath)
        elif 'open videos' in query:
            codePath = "C:\\Users\\Sameeksha S Kotian\\Videos"
            os.startfile(codePath)
        elif 'open images' in query:
            codePath = "C:\\Users\\Sameeksha S Kotian\\Pictures"
            os.startfile(codePath)
            speak("Here are some of the images")
        elif 'bye' in query or 'quit' in query:
            speak("Goodbye Sir. Have a graet day!")
            break
        
    