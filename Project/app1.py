import streamlit as st
import datetime
import os
import json

from asr import record_audio, transcribe
from intent_detector import detect_intent, load_intent_data
from response import respond_to_intent
from speech_AI_Voice import speak

# Constants
LOG_FILE = "D:/.vscode/NebulaAI/Project/data/conversations.jsonl"

# Ensure log file exists
def init_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            json.dump([], f)

# Log conversation to file
def log_conversation(user_input, intent, bot_response):
    with open(LOG_FILE, 'r+') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "user_input": user_input,
            "intent": intent,
            "bot_response": bot_response
        }
        data.append(entry)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

# Initialize embeddings and labels
embeddings, labels = load_intent_data()

# Streamlit UI
st.set_page_config(page_title="AI Support Bot", layout="centered")
st.title("🤖 Real-Time Support Bot")

if st.button("🎙️ Speak"):
    st.info("Recording...")
    audio_path = record_audio()
    st.success("✅ Done Recording")

    transcript = transcribe(audio_path)
    st.write(f"**📝 Transcript:** {transcript}")

    intent = detect_intent(transcript, embeddings, labels)
    st.write(f"**🤖 Detected Intent:** {intent}")

    response = respond_to_intent(intent)
    st.write(f"**💬 Bot:** {response}")

    # Speak the response
    speak(response)

    # Log the conversation
    log_conversation(transcript, intent, response)

# Optional: Show chat history
with st.expander("🕓 Show Conversation History"):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            try:
                logs = json.load(f)
                for entry in logs[-10:]:
                    st.markdown(f"**You:** {entry['user_input']}")
                    st.markdown(f"**Bot:** {entry['bot_response']}")
                    st.caption(f"🕒 {entry['timestamp']}")
            except json.JSONDecodeError:
                st.warning("⚠️ No valid log data found.")

# Init log file at the end
init_log()
