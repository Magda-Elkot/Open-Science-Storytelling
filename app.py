import streamlit as st
import openai
import pyttsx3
from PIL import Image
import tempfile
import base64
import io
from gtts import gTTS
import json
import requests
import streamlit_lottie as st_lottie

# Set the app title and subtitle with artistic styling
st.markdown(
    """
    <h1 style='text-align: center; color: #FF5733; font-size: 36px;'>Open Science Success Stories</h1>
    <p style='text-align: center; font-size: 18px;'>Welcome to our Streamlit web application dedicated to the fascinating world of open science storytelling!</p>
    """,
    unsafe_allow_html=True
)

# Display Image
img = Image.open("nasa.png")
# Display image with a border and shadow
st.image(img, width=600, caption='NASA Logo')

# Add a sidebar with updated markdown content
st.sidebar.markdown(
    """
    ## Instructions
    1. Enter your age and interests in the main panel to personalize your experience.

    2. Choose an option from the dropdown menu:
    
       - **Generate Text**: Create a textual story.
        
       - **Generate Speech**: Convert the textual story to audio & give you the option to download it as an MP3 file.
        
       - **Generate Text and Speech**: Display the generated text while listening to the audio.
        
       - **Generate Video**: Enjoy the experience with visualization and get immersed in the magnificent world of open science.
    
    """
    
)

openai.api_key = "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"
user_age = st.text_input("Your Age")
user_interests = st.text_input("Your Interests")

# Generate the success story
st.markdown("---")
option = st.selectbox("Choose an option", ["Generate Text", "Generate Speech", "Generate Text with Speech", "Generate Video"])
if option == "Generate Text" or option == "Generate Text with Speech":
    if st.button("Generate Text"):
        with st.spinner("Generating..."):
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that provides real-world stories."},
                    {"role": "user", "content": f"Can you please provide a real-world open science success story that aligns with my age {user_age} and my strong interest in {user_interests}? I'm looking for a unique narrative that showcases the incredible possibilities that open science has unlocked in the field of {user_interests}. It's important that the story is based on actual events and achievements, not a fictional one."}
                ]
            )
            generated_story = completion.choices[0].message.content

        # Display the generated story with artistic styling
        st.markdown(
            f"""
            <h2 style='text-align: center; color: #FF5733;'>Generated Text Story</h2>
            <p style='text-align: center;'>{generated_story}</p>
            """,
            unsafe_allow_html=True
        )

if option == "Generate Speech" or option == "Generate Text with Speech":
    if st.button("Generate Speech"):
        with st.spinner("Generating..."):
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that provides real-world stories."},
                    {"role": "user", "content": f"Can you please provide a real-world open science success story that aligns with my age {user_age} and my strong interest in {user_interests}? I'm looking for a unique narrative that showcases the incredible possibilities that open science has unlocked in the field of {user_interests}. It's important that the story is based on actual events and achievements, not a fictional one."}
                ]
            )
            generated_story = completion.choices[0].message.content

        # Text-to-speech functionality
        tts = gTTS(text=generated_story, lang="en")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio_name = temp_audio.name
            tts.save(temp_audio_name)

        # Display the generated speech using Audio widget
        st.markdown("---")
        st.markdown(
            f"""
            <h2 style='text-align: center; color: #FF5733;'>Generated Speech</h2>
            <p style='text-align: center;'>Click the play button to listen:</p>
            """,
            unsafe_allow_html=True
        )
        audio_file = open(temp_audio_name, "rb").read()
        st.audio(audio_file, format="audio/mp3")

        # Provide a download link for the generated speech
        st.markdown("---")
        st.markdown(
            f"""
            <p style='text-align: center;'><a href="data:audio/mp3;base64,{base64.b64encode(audio_file).decode('utf-8')}" download="generated_speech.mp3">Download Generated Speech as MP3</a></p>
            """,
            unsafe_allow_html=True
        )

if option == "Generate Text with Speech":
    if st.button("Generate Text with Speech"):
        with st.spinner("Generating..."):
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that provides real-world stories."},
                    {"role": "user", "content": f"Can you please provide a real-world open science success story that aligns with my age {user_age} and my strong interest in {user_interests}? I'm looking for a unique narrative that showcases the incredible possibilities that open science has unlocked in the field of {user_interests}. It's important that the story is based on actual events and achievements, not a fictional one."}
                ]
            )
            generated_story = completion.choices[0].message.content

        # Text-to-speech functionality
        tts = gTTS(text=generated_story, lang="en")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio_name = temp_audio.name
            tts.save(temp_audio_name)

        # Display the generated story with artistic styling
        st.markdown(
            f"""
            <h2 style='text-align: center; color: #FF5733;'>Generated Text Story</h2>
            <p style='text-align: center;'>{generated_story}</p>
            """,
            unsafe_allow_html=True
        )

        # Display the generated speech using Audio widget
        st.markdown("---")
        st.markdown(
            f"""
            <h2 style='text-align: center; color: #FF5733;'>Generated Speech with Text</h2>
            <p style='text-align: center;'>Click the play button to listen:</p>
            """,
            unsafe_allow_html=True
        )
        audio_file = open(temp_audio_name, "rb").read()
        st.audio(audio_file, format="audio/mp3")

        # Provide a download link for the generated speech with text
        st.markdown("---")
        st.markdown(
            f"""
            <p style='text-align: center;'><a href="data:audio/mp3;base64,{base64.b64encode(audio_file).decode('utf-8')}" download="generated_speech_with_text.mp3">Download Generated Speech with Text as MP3</a></p>
            """,
            unsafe_allow_html=True
        )
        

if option == "Generate Video":
    # Display the video
    video_file_path = "C:\\Users\\Magda\\Desktop\\Videooo.mp4"
    st.video(video_file_path)


   
# Define the course title, description, and website URL
course_title = "Open Science : Exploring the Future of Research"
course_description = """
Ready to embark on an incredible journey? Join us following in the footsteps of the remarkable Dr. Sarah Martinez and pioneering Professor Elena Rodriguez, and countless other passionate scientists. Open science isn't just about stars; it's about expanding your horizons and democratizing scientific knowledge for all, ensuring everyone has a chance to explore the wonders of the universe. 🌌
🔍 Dive into the cosmos of possibilities and enroll in the Open Science 101 course on edX. 🎓 Gain valuable skills, earn badges, and unlock doors to NASA funding opportunities. 🌠 Don't miss this chance to be a part of something extraordinary—let's explore the universe together!


   TOPS caters to all stages of open science journey, including experienced practitioners, those transitioning to new research methods, and students aspiring to start their scientific careers.
"""

course_website_url = "https://github.com/nasa/Transform-to-Open-Science/blob/main/docs/Area2_Capacity_Sharing/Open-Science-101/readme.md"

# Display the course information with the hyperlink
st.markdown(f"## {course_title}")
st.write(course_description)
st.markdown(f"Join the community [Here]({course_website_url})")


# Display Image
img = Image.open("nasa2.png")
# Display image with a border and shadow
st.image(img, width=600)

