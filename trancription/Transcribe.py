import whisper
import os
import glob
import time

def latest():
    print("transcribing...")
    
    time_str = time.strftime("%Y%m%d-%H%M%S")
    latest_file = max(glob.glob('audio/files/*'), key=os.path.getctime)
    model = whisper.load_model("medium")
    result = model.transcribe(latest_file, fp16=False)

    with open(f"trancription/files/{time_str}.txt", "w+") as f:
        f.write(result["text"])

    print("transcription done")
