Real-Time Customer Support Agent Assist & Resolution Bot
A voice-driven AI assistant built with Streamlit, SpeechRecognition, NLP, and TTS, designed to help resolve customer queries in real-time by detecting intent and responding naturally.

Features
Voice Input: Record queries directly from a microphone.

Speech-to-Text: Transcribe audio using pre-trained ASR.

Intent Detection: Match input against predefined intents using Sentence-BERT.

Dynamic Responses: Generate context-based replies.

Text-to-Speech: Convert replies to human-like speech.

Conversation Logging: Store user interactions with timestamps.

Multimodal Ready: Extendable to include audio classification or emotion detection.

Project Structure
Project/
├── app1.py                     # Main Streamlit interface
├── asr.py                      # Audio recording and transcription
├── config.py                   # Configurations for paths and model names
├── intent_detector.py          # Intent matching using Sentence-BERT
├── response.py                 # Rule-based response generator
├── run_bot.py                  # Will run recording, transcription, intent detection and AI voive reply in terminal
├── speech_AI_Voice.py          # Text-to-Speech engine
├── audio_classifier.py         # (Optional) Audio emotion classification
├── data/
│   ├── intent_data.json        # Predefined intents and sample utterances
│   └── conversations.jsonl     # Log of past user-bot conversations
Setup Instructions
1. Clone the Repository
git clone https://github.com/CodeWitheSmile/Real-Time-AI-Calling-Assist-Bot.git
cd Real-Time-AI-Calling-Assist-Bot

2. Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
If requirements.txt is not available, install manually:
pip install streamlit sentence-transformers sounddevice scipy SpeechRecognition pyttsx3

3. Prepare Data
Ensure the following files are in place:

data/intent_data.json: Contains your training examples and intents.

data/conversations.jsonl: (Auto-created) For logging chats.

Sample intent_data.json format:

[
  {
    "intent": "greeting",
    "examples": ["hello", "hi", "hey", "good morning"]
  },
  {
    "intent": "goodbye",
    "examples": ["bye", "see you", "good night"]
  }
]
Running the App
bash
Copy
Edit
streamlit run app1.py
How It Works
Record Audio:
Captures a few seconds of voice input when "🎙️ Speak" button is clicked.

Transcription:
Audio is passed to a speech recognition model which returns a clean transcript.

Intent Detection:
The transcript is encoded with Sentence-BERT and compared to pre-trained intent vectors.

Response:
A rule-based engine returns a contextually appropriate reply, and it's vocalized via TTS.

Log:
All conversations are appended to conversations.jsonl for analysis.

Example Interaction
User: "I need help with my internet connection"
Bot: "Sure! Can you tell me if your router is showing any red lights?"

Optional Extensions
audio_classifier.py: Add emotion-aware responses.

Build a dashboard to show metrics like intent frequency, satisfaction scores, etc.
Multilingual support using translation APIs.


Fina

Inspired by real-world voice-driven customer support systems.
