import os
import google.generativeai as genai
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

# Load the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Extract the transcript from the YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("v=")[-1].split("&")[0]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = " ".join([i["text"] for i in transcript_text])

        return transcript

    except Exception as e:
        raise e

# Generate content using Google Gemini
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)

        if response and hasattr(response, 'text'):
            return response.text
        else:
            return "No summary available from the AI."

    except Exception as e:
        st.error(f"Failed to generate summary: {e}")
        return None
