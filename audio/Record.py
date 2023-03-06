import pyaudio
import wave
from pydub import AudioSegment
import time
import os

AUDIO_INPUT_NAME = "arctis 7 chat"
AUDIO_OUTPUT_NAME = "arctis 7 game"

def inputAudio():
    time_str = time.strftime("%Y%m%d-%H%M%S")

    # Set parameters for audio recording
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    WAVE_OUTPUT_FILENAME = f"audio/files/{time_str}.wav"
    MP3_OUTPUT_FILENAME = f"audio/files/{time_str}.mp3"

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open audio stream for recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    print("Recording... Press CTRL+C to stop recording")

    try:
        # Record audio until user interrupts program
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    print("Recording stopped")

    # Stop and close audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save recorded audio to WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Convert WAV to MP3 using Pydub
    audio = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
    audio.export(MP3_OUTPUT_FILENAME, format="mp3")

    # Delete WAV file
    os.remove(WAVE_OUTPUT_FILENAME)