import os
import glob
import time
import openai

def latest():
    latest_file = max(glob.glob('trancription/files/*'), key=os.path.getctime)
    transcribed_text = open(latest_file, "r").read().strip()
    print(transcribed_text)