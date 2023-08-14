# Interactive Voice Assistant (ALPHA)

ALPHA is an interactive voice assistant built using Python that can understand and respond to both text and speech input. It performs tasks like opening apps, playing music, answering queries, and engaging in conversations.

## Features

- **Speech Recognition and Text-to-Speech Conversion:** ALPHA can convert speech input to text and text to speech using the `speech_recognition` and `pyttsx3` libraries.

- **App Opening:** Open applications by saying "Open app [app_name]" or typing "open app [app_name]" in the input.

- **Music Playback:** ALPHA can play music on YouTube. Just say "Play music [song_name]" or type "play music [song_name]".

- **Query Handling:** Ask ALPHA questions like "What is your name?" or "What's the current time?" for relevant responses.

- **Chatbot Interaction:** ALPHA uses the RapidAPI-powered ChatGPT-3.5 for dynamic conversations.

## Usage

1. Clone or download this repository.
2. Install required libraries: `pip install requests pyttsx3 speech_recognition`
3. Get your RapidAPI key from https://rapidapi.com/ and replace `"YOUR_RAPIDAPI_KEY"` in the code.
4. Run `voice_assistant.py` and choose text (1) or speech (2) input.
5. Interact with ALPHA through input or speech.

## Examples

- **Text Input:**
You: [Speak] "Open app calculator."
ALPHA: Opening application: calculator.

## Note

- Ensure your system has a working microphone for speech input.
- ALPHA's performance relies on speech recognition accuracy and GPT-3.5 chatbot responses.

## Contributors

- Developed by Jagdeep Singh.
- Contributions, issues, and enhancements welcome.

## License

This project is licensed under the [MIT License](LICENSE).
