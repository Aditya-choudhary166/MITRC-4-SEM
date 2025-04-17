import speech_recognition as sr
import pyttsx3
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results. Please check your internet connection.")
        return ""

def jarvis():
    speak("Hello Aditya, how can I assist you?")
    while True:
        command = listen()
        
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        
        elif "wikipedia" in command:
            speak("Searching Wikipedia...")
            command = command.replace("wikipedia", "")
            try:
                result = wikipedia.summary(command, sentences=2)
                speak(result)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find any results.")

        else:
            speak("I am not programmed for that yet.")

if __name__ == "__main__":
    jarvis()
