import webbrowser
import requests
import json
import pyttsx3
import speech_recognition as sr
import datetime
import subprocess
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        user_input = r.recognize_google(audio)
        print("You:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""
    except sr.RequestError as e:
        print("Sorry, an error occurred. Please try again.")
        return ""

def play_music(song_name):
    try:
        query = song_name + " on YouTube"
        url = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(url)
    except Exception as e:
        print(f"Error playing music: {e}")
        speak(f"Error playing music: {e}")

def open_app(app_name):
    try:
        subprocess.pPoen(app_name)
    except FileNotFoundError:
        print(f"App not found: {app_name}")
        speak(f"App not found: {app_name}")
    except Exception as e:
        print(f"Error opening app: {e}")
        speak(f"Error opening app: {e}")

def get_date_time():
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%Y-%m-%d")
    time = current_datetime.strftime("%H:%M:%S")
    return date, time

def ALPHA(message):
    
    if message.lower().startswith("open "):
        url = message[5:]
        print("Opening website:", url)
        webbrowser.open(url)
        return
    
    # calling api 
    url = "https://chatgpt53.p.rapidapi.com/"
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "reset"
            },
            {
                "role": "user",
                "content": message
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "your api key here",
        "X-RapidAPI-Host": "chatgpt53.p.rapidapi.com"
    }



    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)

        choices = data["choices"]
        if choices:
            for choice in choices:
                message = choice.get("message")
                if message and "role" in message and "content" in message:
                    role = message["role"]
                    content = message["content"]
                    if role == "assistant":
                        print("ALPHA:", content)
                        speak(content)
        else:
            print("Error: No choices in the API response")
            speak("Error: No choices in the API response")
    else:
        print("Error: API request failed")
        speak("Error: API request failed")


choice = input("Enter '1' to input text or '2' to input speech: ")
while True:
    if choice == '1':
        user_input = input("You: ")
        if user_input.lower() == '' or user_input.lower() == ' ':
            response="No input. How can I help you?"
            print("ALPHA : ",response)
            speak(response)
        elif user_input.lower().startswith("open app "):
            app_name = user_input[9:]
            open_app(app_name)
        elif user_input.lower().startswith("play music"):
            song_name = user_input[11:]
            play_music(song_name)
        elif user_input.lower() == 'what is your name?'or user_input.lower() == 'whats ur name' :
            response="I am ALPHA. I am designed by the team of developers in chandighar university."
            print("ALPHA : ",response)
            speak(response)
        elif 'time' in user_input.lower() or 'date' in user_input.lower():
            current_date, current_time=get_date_time()
            response = f"The current time is {current_time} and The current date is {current_date}"
            print("ALPHA:", response)
            speak(response)
            pass        
        elif user_input.lower()=="exit":
            print("Thankyou for using")
            speak("Thankyou for using")
            print("-----------------------------------------------------")
            break
        else:
            ALPHA(user_input)
        
    elif choice == '2':
        user_input = listen()
        if user_input.lower() == '' or user_input.lower() == ' ':
            response="No input. How can I help you?"
            print("ALPHA : ",response)
            speak(response)
        elif user_input.lower().startswith("open app "):
            app_name = user_input[9:]
            open_app(app_name)
        elif user_input.lower().startswith("play music "):
            song_name = user_input[11:]
            play_music(song_name)
        elif user_input.lower() == 'what is your name?'or user_input.lower() == 'whats ur name' :
            response="I am ALPHA. I am designed by the team of developers in chandighar university."
            print("ALPHA : ",response)
            speak(response)
        elif 'time' in user_input.lower() or 'date' in user_input.lower():
            current_date, current_time=get_date_time()
            response = f"The current time is {current_time} and The current date is {current_date}"
            print("ALPHA:", response)
            speak(response)
            pass        
        elif user_input.lower()=="exit":
            print("Thankyou for using")
            speak("Thankyou for using")
            print("-----------------------------------------------------")
            break
        else:
            ALPHA(user_input)
