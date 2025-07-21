from faster_whisper import WhisperModel
import pyaudio
import wave

# Load the Whisper model once globally
model = WhisperModel("base", compute_type="int8")  # Alternatives: "medium", "large", etc.

def record_audio(filename="temp.wav", duration=5):
    RATE = 44100
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("🎙️ Recording...")
    frames = [stream.read(CHUNK) for _ in range(int(RATE / CHUNK * duration))]
    print("✅ Done Recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    return filename  

def transcribe(filename="temp.wav"):
    segments, _ = model.transcribe(filename)  
    transcript = " ".join(segment.text for segment in segments)
    return transcript
