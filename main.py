import speech_recognition as sr 
import webbrowser
import pyttsx3
import musiclibrary


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processcommand(c):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn.")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        speak(f"Playing {song}")
   

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        #Listen for wake word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()


        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2,phrase_time_limit=1)
                word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)
                    
        except Exception as e:
            print("Error; {0}".format(e))
        

