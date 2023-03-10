# AutoNote

(work in progress)

AutoNote is a python project that automatically transcribes and summarizes audio files using Whisper speech recognition and OpenAI language models. Originally the idea stemmed from me wanting to automate my note-taking in meetings.

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

## Contributing

The project is still in its infancy and its future unclear, but AutoNote is an open-source project and contributions are welcome. If you want to contribute, please follow these steps:

1. Fork this repository: https://github.com/Ekoda/AutoNote/fork
2. Create your feature branch: `git checkout -b feature/fooBar`
3. Commit your changes: `git commit -am 'Add some fooBar'`
4. Push to the branch: `git push origin feature/fooBar`
5. Create a new pull request: https://github.com/Ekoda/AutoNote/compare
