import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
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
def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.send('youremail@gmail.com', to, content)
    server.close()


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
        
        # crete a random function to generate song index
        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        # format datetime string
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H-%M-%S')
            speak(f"The time is{strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)
        
        elif 'send email' in query:
            try:
                speak("What's the message?")
                content = takeCommand()
                to = "sehajkahlon437@gmail.com"
                sendEmail(to , content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I was'nt able to sent the email. Please try again")
            
        

