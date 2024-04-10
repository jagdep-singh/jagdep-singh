from flask import Flask, render_template, request
import subprocess
import webbrowser
import requests
import json
import pyttsx3
import speech_recognition as sr
import datetime

app = Flask(__name__)

messages = []

def play_music(song_name):
    try:
        query = song_name + " on YouTube"
        url = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(url)
    except Exception as e:
        print(f"Error playing music: {e}")

def open_app(app_name):
    try:
        subprocess.Popen(app_name)
    except FileNotFoundError:
        print(f"App not found: {app_name}")
    except Exception as e:
        print(f"Error opening app: {e}")

def ALPHA(message):
    if message.lower().startswith("open "):
        url = message[5:]
        print("Opening website:", url)
        webbrowser.open(url)
        return "Opening website: " + url

    # calling api
    url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "your_api_key",
        "X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        try:
            # Access the first choice's message content
            content = data['choices'][0]['message']['content']
            print("ALPHA: ", content)
            return content
        except (KeyError, IndexError):
            print("Error: Could not extract content from the response.")
            return "Sorry, I couldn't understand."
    else:
        print("Error:", response.status_code)
        return "Sorry, an error occurred. Please try again."

def get_date_time():
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%Y-%m-%d")
    time = current_datetime.strftime("%H:%M:%S")
    return date, time

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form['user_input']
    output = None

    
    messages.append({'type': 'user', 'content': user_input})

    if user_input.lower() == '' or user_input.lower() == ' ':
        response = "No input. How can I help you?"
        output = response
    elif user_input.lower().startswith("open app "):
        app_name = user_input[9:]
        output = f"Opening {app_name}..."
        open_app(app_name)
    elif user_input.lower().startswith("play"):
        song_name = user_input[5:]
        output = f"Playing {song_name} on YouTube..."
        play_music(song_name)
    elif user_input.lower() == 'what is your name?' or user_input.lower() == 'whats ur name':
        response = "I am ALPHA. I am designed by the team of developers in Chandigarh University.\n1.Bhupati Parmar\n2.Aditya Shikot\n3.Jagdeep Singh"
        output = response
        
    elif 'time' in user_input.lower() or 'date' in user_input.lower():
        current_date, current_time = get_date_time()
        response = f"The current time is {current_time} and The current date is {current_date}"
        output = response
    elif 'exit()' in user_input.lower():
        output = "Thankyou for using ALPHA."
        
    
    else:
        output = ALPHA(user_input)

    
    messages.append({'type': 'assistant', 'content': output})

    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
