# Speech-to-Speech Conversational Bot

## Introduction
The **Speech-to-Speech Conversational Bot** is a real-time voice interaction system that combines cutting-edge technologies to enable seamless, intuitive conversations. It utilizes advanced language models and speech processing tools to provide a natural and engaging user experience. 

## Features
- **Speech Input**: Records user audio through the interface.
- **Real-time Transcription**: Converts speech to text using **OpenAI Whisper V3 Turbo** via Groq's inference client.
- **Intelligent Responses**: Generates context-aware responses using **LLaMA 3.3-80B**.
- **Speech Output**: Converts responses back to speech using **gTTS** for natural voice playback.
- **User Interface**: Built with **Streamlit** for easy interaction and audio visualization.

## Stack Design
- **Frontend**: Streamlit for audio recording and response display.
- **Speech-to-Text**: OpenAI Whisper V3 Turbo accessed through Groq's inference client.
- **Language Model**: LLaMA 3.3-80B for generating intelligent and conversational responses.
- **Text-to-Speech**: gTTS for converting text back to speech.

## Workflow
1. **Audio Recording**: The user records their query using the Streamlit interface.
2. **Speech Transcription**: The recorded audio is sent to the **Whisper V3 Turbo** model via Groq's inference client for transcription.
3. **Response Generation**: The transcribed text is passed to the **LLaMA 3.3-80B** model to generate a contextually appropriate response.
4. **Speech Synthesis**: The generated response is converted back into speech using **gTTS**.
5. **Playback**: The audio response is played back to the user through the interface.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/speech-to-speech-bot.git
   cd speech-to-speech-bot
