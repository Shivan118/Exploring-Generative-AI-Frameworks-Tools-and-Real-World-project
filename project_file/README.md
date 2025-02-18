# YouTube Transcript to Summary Converter

This project allows users to convert YouTube video transcripts into summarized notes. It leverages Google Gemini AI for summarization and is implemented using both Streamlit and Flask frameworks. Below are the instructions and details for each version of the application.

## Table of Contents
- [Streamlit Version](#streamlit-version)
- [Flask Version](#flask-version)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Design](#design)
- [Helper Functions](#helper-functions)

## Streamlit Version

### Overview
This section provides details about the Streamlit application.

### Folder Structure for Streamlit & Flask Version
```
project_root/
│
├── streamlit_app/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── design.py
│   │   └── helpers.py
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
└── flask_app/
    ├── app.py
    ├── templates/
    │   └── index.html
    ├── static/
    │   └── styles.css
    │   └── script.js
    ├── requirements.txt
    └── .env

```

## Setup Instructions

##### 1. Clone the repository:
```bash
git clone <repository_url>
cd flask_app
```

##### 2. Create a virtual environment (optional but recommended):
```bash
conda create -p env python=3.10 -y
conda activate env/   # On Windows 
```

##### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

##### 4. Add your Google API Key in the .env file:
```bash
GOOGLE_API_KEY=your_google_api_key
```

##### 5. Run the Flask or Streamlit application:
```bash
python app.py
```

## Usage
- Open the application in your web browser (default is http://localhost:5000).
- Enter the YouTube video link and click "Get Detailed Notes" to receive the summary.

## Design
Both applications feature a simple and intuitive UI. The Streamlit version leverages built-in Streamlit components, while the Flask version uses HTML and CSS for styling.

## Streamlit UI
Users can input a YouTube link and get a summarized version of the transcript.

## Flask UI
A form to input the YouTube link and a section to display the summary.

## Helper Functions
The utils folder contains helper functions that can be reused across the applications.

```helpers.py```
This file includes functions for:

- Extracting YouTube video transcripts.
- Generating summaries using Google Gemini AI.

```design.py```
This file includes functions for:
- Applying styles and templates for the application.
