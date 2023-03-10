import sys
from audio import Record
from trancription import Transcribe
from summarization import Summarize

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "record":
            record = Record.recordInput()
        elif sys.argv[1] == "transcribe":
            transcribe = Transcribe.latest()
        elif sys.argv[1] == "summarize":
            summarize = Summarize.latest()
        else:
            print("Invalid argument. Usage: python3 main.py [record/transcribe/summarize]")
    else:
        Record.inputAudio()
        Transcribe.latest()
        Summarize.latest()
