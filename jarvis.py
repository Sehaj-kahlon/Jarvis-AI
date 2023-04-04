import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hey, I'm Jarvis, how can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshould = 1
        audio = r.listen(source)
    
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language  ='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I did'nt get that. Please try saying again")
        return "None"
    return query


if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('http://www.google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('http://www.stackoverflow.com')
    
