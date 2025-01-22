import os
import sys
import datetime
import dotenv
import streamlit as st
from groq import Groq
from gtts import gTTS
import time

# load the environment variables
dotenv.load_dotenv()

# create a groq client
client = Groq()

# the function to query the groq inference endpoint for speech to text using the whisper v3 large turbo model
def query_groq_whisper_stt(filename):
    try:
        with open(filename, "rb") as file:

            transcription = client.audio.transcriptions.create(
            file=(filename, file.read()), 
        model="whisper-large-v3-turbo",
          prompt="Specify context or spelling",

         response_format="json",
            language="en",
             temperature=0.0
            )

            return transcription.text
    except Exception as e:
        return "there was an error during transcription so please tell the user to try again"


# the function to save the audio file
def save_audio_file(audio_in_bytes, file_extension):
    timestamp = datetime.datetime.now().strftime("_%Y%m%d_%H%M%S") 

    file_name = f"audio_{timestamp}.{file_extension}"

    with open(file_name, "wb") as f:
        f.write(audio_in_bytes.read())

    return file_name


# the function to query the groq inference endpoint for chat completion using the llama 3.3 70b versatile model
def query_groq_llm(text):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpful assistant, that can help users with their queries and answer them in a friendly manner. make sure to generate responses in short way like for 10-15 seconds of say.",
                },{
                    "role": "user",
                    "content": f"{text}",
                   }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.2,
         max_completion_tokens=128,
             top_p=1,
        stop=None,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    
    except Exception as e:
        return "There was an error during chat completion so please tell the user to try again after some time" 
    
# the function to query the google text to speech library for text to speech
def query_gtts(text, ai_audio_file_path):
    try:
        tts = gTTS(text=text, lang="en")
        tts.save(ai_audio_file_path)
        return tts

    except Exception as e:
        return "There was an error during TTS please try again after some time"

# the main function
def main():
    st.title("Speech to Speech LLM Bot")    

    tab1 = st.tabs(["Record Audio"])[0]

    audio_file_path = None
    
    with tab1:
        st.subheader("Click the microphone to start and stop the recording")
        audio_bytes = st.audio_input(" ")
        start = time.time()
        if audio_bytes:
                st.header("User Query")
                st.divider()
                st.audio(audio_bytes, format="audio/wav")
                audio_file_path = save_audio_file(audio_bytes, "wav")

    # if the audio file path is not None, then query the groq whisper stt endpoint and the groq llm endpoint
    if audio_file_path:
        try:

            # query the groq whisper stt endpoint
            transcript_text = query_groq_whisper_stt(audio_file_path)

            # query the groq llm endpoint
            llm_responce = query_groq_llm(transcript_text)
            ai_audio_file_path = audio_file_path.replace("wav", "mp3")
            
            # query the google text to speech library
            query_gtts(llm_responce, ai_audio_file_path)
            end = time.time()

            st.header("AI Responce")

            st.audio(ai_audio_file_path, format="audio/mp3", loop=False, start_time=0, autoplay=True)
            st.header("Responce time")
            st.write(f"Time taken to generate responce: {end-start} seconds")
        except Exception as e:
            st.error(f"Error during transcription: {e}")
        finally:
            # remove the audio file
            if audio_file_path and os.path.exists(audio_file_path):
                os.remove(audio_file_path)
                os.remove(ai_audio_file_path)


# run the main function
if __name__ == "__main__":
    working_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(working_dir)
    main()
