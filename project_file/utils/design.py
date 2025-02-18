import streamlit as st

# Function to display the input fields for the user
# Function to display the UI for input
def display_ui():
    youtube_link = st.text_input("Enter YouTube Video Link:")

    if youtube_link:
        try:
            video_id = youtube_link.split("v=")[-1].split("&")[0]  # More robust YouTube ID extraction
            st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
        except IndexError:
            st.error("Invalid YouTube link. Please enter a valid URL.")
    
    if st.button("Get Detailed Notes"):
        return youtube_link
    
    return None

# Function to display the generated summary
def display_summary(summary):
    if summary:
        st.markdown("## Detailed Notes:")
        st.write(summary)
    else:
        st.write("No summary available to display.")