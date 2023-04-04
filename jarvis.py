import pyttsx3
import datetime
import speachRecognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Afternoon!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hey, I'm Jarvis, how can i help you")


def takeCommand():
    r = sr.Rcongnizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshould = 1


if __name__ == "__main__":
    WishMe()
