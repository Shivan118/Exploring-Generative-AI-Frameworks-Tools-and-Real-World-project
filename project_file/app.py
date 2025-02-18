import streamlit as st
from dotenv import load_dotenv
from utils.design import display_ui, display_summary
from utils.helper import extract_transcript_details, generate_gemini_content
import os
import google.generativeai as genai

load_dotenv()  # Load environment variables

# Load the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Prompt to be used for generating content
prompt = """
You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  
"""

# Main app function
# Main app function
def main():
    st.title("YouTube Transcript to Detailed Notes Converter")

    # Display the input UI
    youtube_link = display_ui()

    if youtube_link:
        try:
            # Get transcript from YouTube
            transcript_text = extract_transcript_details(youtube_link)

            # Generate summary using Google Gemini AI
            if transcript_text:
                summary = generate_gemini_content(transcript_text, prompt)

                # Display the summary
                display_summary(summary)
        except Exception as e:
            st.error(f"Error: {e}")
if __name__ == "__main__":
    main()