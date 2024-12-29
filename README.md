# Text-to-Speech Conversion Application

## Overview
This application is designed to convert text into speech, supporting multiple languages and customizable voices. Users can input text, select their preferred language and voice settings, and generate corresponding audio output. The application offers both online (using Google TTS) and offline (using pyttsx3) speech synthesis options. It is a versatile tool that allows users to save the generated audio files and customize the speech synthesis settings such as voice type and speech rate.

---

## Project Details

- **Name**: Text-to-Speech Conversion Application  
- **Developer**: A Mohammed Faazil  
- **Company**: Personal Project  
- **Internship ID**: CT08EHJ 
- **Domain**: Machine Learning / Speech Synthesis  
- **Duration**: Custom Project

---

## Features

1. **Multi-language Support**: Users can select from various language options for speech synthesis.
2. **Customizable Voices**: Allows selection between male and female voices and adjustable speech rate.
3. **Online Support**: Utilizes Google TTS for high-quality, multi-language speech generation.
4. **Offline Support**: Employs pyttsx3 for text-to-speech conversion without requiring an internet connection.
5. **Save Audio Output**: Users can save the generated speech as an MP3 file.
6. **Interactive Interface**: Provides a CLI-based interface for easy user interaction.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `gTTS`: For online text-to-speech synthesis.
  - `pyttsx3`: For offline text-to-speech conversion with customizable voices.
  - `os`: To handle file operations and play audio.

---

## Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/text-to-speech-app.git
   cd text-to-speech-app
   ```

2. **Install Required Libraries**:
   ```bash
   pip install gtts pyttsx3
   ```

3. **Run the Application**:
   ```bash
   python tts_app.py
   ```

4. **Follow the Instructions**:
   - Choose the desired text-to-speech engine.
   - Enter the text, language, voice type, and other preferences.
   - Save the audio file if required.

---

## Example Usage

### Online Mode (Google TTS):
- Input: `Hello, this is a text-to-speech test.`
- Language: `en` (English)
- Output: Audio file or direct playback.

### Offline Mode (pyttsx3):
- Input: `Bienvenue dans l'application TTS.`
- Voice: Female
- Rate: 150

---

## Future Enhancements

1. Add a web interface using Flask or Streamlit for broader accessibility.
2. Include advanced TTS systems like Coqui TTS or Hugging Face models for enhanced voice options.
3. Implement batch processing for handling multiple text files.
4. Integrate real-time speech playback using libraries like `pyaudio`.

---
