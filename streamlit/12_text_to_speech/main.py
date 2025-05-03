# writing a code to convert text to speech using gTTS
# # This script uses the gTTS library to convert text to speech and save it as an MP3 file.
# # It includes a simple Streamlit interface for user input and audio playback.
# # Requirements: streamlit, gTTS
#
import streamlit as st
from gtts import gTTS
import os
import tempfile
import base64
import requests

# Function to convert text to speech and save as MP3
def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        tts.save(tmp_file.name)
        return tmp_file.name

# Function to download the MP3 file
def download_file(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    b64 = base64.b64encode(file_data).decode()
    href = f'<a href="data:file/mp3;base64,{b64}" download="{os.path.basename(file_path)}">Download MP3</a>'
    return href

# Function to play the audio file in Streamlit
def play_audio(file_path):
    audio_file = open(file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    audio_file.close()

# Streamlit app
# Set the title and description
st.title('🎤 Text to Speech Converter' )
st.write('Convert your text into speech and download it as an MP3 file.')
st.write('Enter the text you want to convert to speech and select the language.')

# Text input for user to enter text
text_input = st.text_area('Enter text:', height=150, placeholder='Type your text here...')

# Language selection
lang = st.selectbox('Select language:', ['en', 'es', 'fr', 'de', 'it', 'pt'])
# Language codes: 'en' for English, 'es' for Spanish, 'fr' for French, 'de' for German, 'it' for Italian, 'pt' for Portuguese

# Add more languages as needed
# Example: 'ja' for Japanese, 'zh' for Chinese, etc.
# Add a button to convert text to speech
if st.button('Convert to Speech'):
    if text_input:
        with st.spinner('Converting...'):
            try:
                # Convert text to speech and save as MP3
                mp3_file_path = text_to_speech(text_input, lang)
                st.success('Conversion successful!')
                
                # Play the audio file
                play_audio(mp3_file_path)
                
                # Provide download link for the MP3 file
                download_link = download_file(mp3_file_path)
                st.markdown(download_link, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to convert.")

# Clean up temporary files
if 'mp3_file_path' in locals():
    os.remove(mp3_file_path)  # Remove the temporary file after use
# Note: The above code uses gTTS for text-to-speech conversion and Streamlit for the web interface.
# Make sure to install the required libraries using pip:
# pip install streamlit gTTS requests
# Run the Streamlit app using the command: streamlit run main.py
# Open the app in your web browser at the URL provided in the terminal.
# You can enter text, select a language, and convert it to speech. The generated audio can be played and downloaded as an MP3 file.
# The app is simple and user-friendly, allowing for easy text-to-speech conversion.
# You can further enhance the app by adding more features, such as adjusting the speech speed, voice selection, or additional languages.
# This can be done by modifying the gTTS parameters or using other libraries for more advanced text-to-speech capabilities.
# The app can be deployed on platforms like Streamlit Sharing, Heroku, or any other cloud service that supports Python web applications.

