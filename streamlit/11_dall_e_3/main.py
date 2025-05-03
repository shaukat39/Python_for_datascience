# DALL·E 3 Image Generation with Streamlit
# This script uses the OpenAI API to generate images based on user prompts using DALL·E 3.
# It includes a simple Streamlit interface for user input and image display.
# Requirements: streamlit, openai, requests, Pillow

import streamlit as st
from openai import OpenAI
import requests
from io import BytesIO

# Initialize the OpenAI client
client = OpenAI(api_key="enter your api key here")  # Or use environment variable

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,  # Number of images to generate
        size="1024x1024",  # Image size
        quality="standard"
    )
    return response

def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        return BytesIO(response.content)
    return None

def main():
    st.title('🎨 DALL·E 3 Image Generator')
    prompt = st.text_input('Enter a prompt for DALL·E 3:', '')

    if st.button('Generate Image'):
        if not prompt.strip():
            st.warning("Please enter a prompt.")
            return

        with st.spinner('Generating Image...'):
            try:
                response = generate_image(prompt)
                if response and response.data:
                    image_url = response.data[0].url
                    st.image(image_url, caption='Generated Image', use_column_width=True)

                    # Download functionality
                    image_buffer = download_image(image_url)
                    if image_buffer:
                        st.download_button(
                            label="Download Image",
                            data=image_buffer,
                            file_name="generated_image.png",
                            mime="image/png"
                        )
                    else:
                        st.error("Failed to download image.")
                else:
                    st.error('No image was returned. Try a different prompt.')
            except Exception as e:
                st.error(f"Error generating image: {e}")

if __name__ == '__main__':
    main()
