import os
import glob
import time
from summarization import Api

def latest():
    print("summarizing...")
    time_str = time.strftime("%Y%m%d-%H%M%S")
    latest_file = max(glob.glob('trancription/files/*'), key=os.path.getctime)
    transcribed_text = open(latest_file, "r").read().strip()
    maxLength = 5000
    meeting_notes = ""
    if len(transcribed_text) > maxLength:
        splitted_notes = [transcribed_text[i:i+maxLength] for i in range(0, len(transcribed_text), maxLength)]
        summarized_notes = []
        for i, note in enumerate(splitted_notes):
            summarized_note = Api.summarize(note)
            summarized_notes.append(summarized_note)
            print(i + 1, "of", len(splitted_notes), "notes summarized")
        meeting_notes = " ".join(summarized_notes)
        print(meeting_notes)
    else:
        meeting_notes = Api.summarize(transcribed_text)
    with open(f"summarization/files/{time_str}.txt", "a+") as f:
        f.write(meeting_notes)
    print("summarization done")

