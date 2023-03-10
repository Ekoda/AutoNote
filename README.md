# AutoNote

(work in progress)

AutoNote is a python project that automatically transcribes and summarizes audio files using Whisper speech recognition and OpenAI language models. Originally the idea stemmed from me wanting to automate my note-taking in meetings.

The results will vary depending on audio, model and of course meeting quality. Vague and opaque meetings will produce simliar results. However, I expect the future to bring vasts improvements in both transcription and language models, perhaps advancements in multi modal language models will allow us to skip the transcription step altogether - incredible results will follow.

## Features

- Transcribe audio files in various formats (wav, mp3, etc) using the Whisper speech recognition model from OpenAI
- Summarize transcribed text using OpenAI language models such as GPT-3 or Codex
- Save transcribed and summarized text as txt files
- Record audio from microphone then transcribe and summarize it
- Run the project as a command-line tool

## Installation

To install AutoNote, you need to have python 3.7 or higher and pip installed on your system. Then, follow these steps:

1. Clone this repository: `git clone https://github.com/Ekoda/AutoNote.git`
2. Navigate to the project directory: `cd AutoNote`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up your OpenAI API key by creating a .env file at the root of your project and put your openAI API key in as: OPENAI_API_KEY = "MY_API_KEY"
5. Run the main.py file: `python main.py` to record, transcribe and summarize the latest file added. You can also use arguments such as: `python main.py transcribe` to run only one of the segments

## Contributing

The project is still in its infancy and its future unclear, but AutoNote is an open-source project and contributions are welcome. If you want to contribute, please follow these steps:

1. Fork this repository: https://github.com/Ekoda/AutoNote/fork
2. Create your feature branch: `git checkout -b feature/fooBar`
3. Commit your changes: `git commit -am 'Add some fooBar'`
4. Push to the branch: `git push origin feature/fooBar`
5. Create a new pull request: https://github.com/Ekoda/AutoNote/compare
