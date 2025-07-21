import json
from datetime import datetime

def log_conversation(transcript, intent, response, log_file="D:/.vscode/NebulaAI/Project/data/conversations.jsonl"):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_input": transcript,
        "intent": intent,
        "bot_response": response
    }
    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
