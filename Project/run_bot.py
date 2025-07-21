from asr import record_audio, transcribe
from intent_detector import detect_intent, load_intent_data
from response import respond_to_intent
from speech_AI_Voice import speak
from logger import log_conversation 

# Load intent training data
embeddings, labels = load_intent_data()

# Step 1: Record and transcribe
audio_path = record_audio()
transcript = transcribe(audio_path)
print("📝 Transcript:", transcript)

# Step 2: Detect intent using transcript + trained data
intent = detect_intent(transcript, embeddings, labels)
print("🤖 Detected Intent:", intent)

response = respond_to_intent(intent)
print("💬 Bot:", response)

speak(response)
log_conversation(transcript, intent, response)