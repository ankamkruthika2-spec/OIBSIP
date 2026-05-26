import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am your voice assistant")

while True:

    command = input("Enter command: ").lower()

    if command == "hello":
        speak("Hello, nice to meet you")

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + current_time)

    elif command == "date":
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif command == "google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif command == "youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command == "bye":
        speak("Goodbye")
        break

    else:
        speak("Sorry, I don't understand")
