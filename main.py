
!pip install gtts pyttsx3 playsound

import pyttsx3
from gtts import gTTS
import os

def tts_gtts(text, lang="en", save_as_file=False, filename="output.mp3"):
    """
    Text-to-Speech using gTTS (Google Text-to-Speech)
    """
    try:
        # Generate speech
        tts = gTTS(text=text, lang=lang, slow=False)
        if save_as_file:
            tts.save(filename)
            print(f"Audio saved as: {filename}")
        else:
            # Play directly
            tts.save("temp.mp3")
            os.system("start temp.mp3" if os.name == "nt" else "open temp.mp3")
    except Exception as e:
        print(f"Error using gTTS: {e}")

def tts_pyttsx3(text, voice="male", rate=150):
    """
    Text-to-Speech using pyttsx3 (Offline)
    """
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")

        # Set voice
        if voice == "female":
            engine.setProperty("voice", voices[1].id)
        else:
            engine.setProperty("voice", voices[0].id)

        # Set speech rate
        engine.setProperty("rate", rate)

        # Speak
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error using pyttsx3: {e}")

def main():
    print("Welcome to Text-to-Speech Application!")
    print("Choose the TTS engine:")
    print("1. Google TTS (gTTS - Online, supports multiple languages)")
    print("2. pyttsx3 (Offline, customizable)")

    choice = input("Enter your choice (1/2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice. Exiting.")
        return

    text = input("Enter the text you want to convert to speech: ")

    if choice == "1":
        lang = input("Enter the language code (e.g., 'en' for English, 'es' for Spanish): ")
        save_option = input("Do you want to save the audio file? (yes/no): ").lower()
        save_as_file = save_option in ["yes", "y"]
        tts_gtts(text, lang, save_as_file)
    else:
        voice = input("Choose voice (male/female): ").lower()
        rate = int(input("Enter the speech rate (default is 150): "))
        tts_pyttsx3(text, voice, rate)

if __name__ == "__main__":
    main()
