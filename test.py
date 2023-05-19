import streamlit as st
from gtts import gTTS
import os
import glob
import time

def text_to_speech(text):
    tts = gTTS(text=text, lang='en', slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


import os

# Specify the path to the directory
directory = "temp"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

    
text = st.text_input("type something", 'Life of Brian')

if st.button("convert"):
    result, output_text = text_to_speech(text)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Your audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    display_output_text = True  # Set this to True if you want to display the output text
    if display_output_text:
        st.markdown(f"## Output text:")
        st.write(f" {output_text}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)

remove_files(7)
