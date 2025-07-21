from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load and encode training data
def load_intent_data(file_path="D:/.vscode/NebulaAI/Project/data/intent_data.json"):
    with open(file_path, 'r') as f:
        data = json.load(f)

    intent_examples = []
    labels = []

    for entry in data:
        intent = entry["intent"]
        for example in entry["examples"]:
            intent_examples.append(example)
            labels.append(intent)

    embeddings = model.encode(intent_examples, convert_to_tensor=True)
    return embeddings, labels

# Match user input to nearest intent
def detect_intent(user_text, embeddings, labels):
    user_embedding = model.encode(user_text, convert_to_tensor=True)
    scores = util.cos_sim(user_embedding, embeddings)[0]
    best_match_index = scores.argmax().item()
    return labels[best_match_index]
