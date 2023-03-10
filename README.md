# AutoNote

(work in progress)

AutoNote is a python project that automatically transcribes and summarizes audio files using Whisper speech recognition and OpenAI language models.

## Features

- Transcribe audio files in various formats (wav, mp3, etc) using the Whisper speech recognition model from OpenAI
- Summarize transcribed text using OpenAI language models such as GPT-3 or Codex
- Save transcribed and summarized text as txt files
- Record audio from microphone and transcribe it
- Run the project as a command-line tool

## Installation

To install AutoNote, you need to have python 3.7 or higher and pip installed on your system. Then, follow these steps:

1. Clone this repository: `git clone https://github.com/Ekoda/AutoNote.git`
2. Navigate to the project directory: `cd AutoNote`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up your OpenAI API key to use the openAI API: https://docs.openai.com/docs/api-reference/authentication
5. Run the main.py file: `python main.py` to record, transcribe or summarize the latest file added use arguments such as: `python main.py transcribe`
