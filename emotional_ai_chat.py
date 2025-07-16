# emotional_ai_chat.py

import openai
from brain import Brain, DNA
import os
import json
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Step 1: Use OpenAI for Sentiment Classification ---
def classify_sentiment_openai(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an emotion classifier. For the input, respond ONLY with one of the following labels: positive, negative, neutral."},
            {"role": "user", "content": f"Classify the sentiment of: '{text}'"}
        ]
    )
    return response["choices"][0]["message"]["content"].strip().lower()

# --- Step 2: Map Sentiment to Emotional Event ---
def update_brain_with_sentiment(brain, sentiment):
    if sentiment == "positive":
        brain.process_event("success")
    elif sentiment == "negative":
        brain.process_event("failure")
    # Neutral events do not change internal state for now

# --- Step 3: Generate System Prompt Based on Brain State ---
def generate_system_prompt(brain):
    emotion = max(["joy", "frustration", "confidence"], key=lambda x: brain.nodes[x].value)
    belief = brain.self_model["belief"]
    goal = brain.choose_goal()
    return f"You are an emotionally evolving AI. You currently feel {emotion}, your belief is '{belief}', and your current goal is to {goal}."

# --- Step 4: Main Interaction Loop ---
def chat_with_user(user_input, brain, memory_log, chat_history):
    sentiment = classify_sentiment_openai(user_input)
    update_brain_with_sentiment(brain, sentiment)
    system_prompt = generate_system_prompt(brain)

    if not chat_history:
        chat_history.append({"role": "system", "content": system_prompt})
    else:
        chat_history[0] = {"role": "system", "content": system_prompt}  # update with new emotional state

    chat_history.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=chat_history
    )
    ai_output = response["choices"][0]["message"]["content"].strip()
    chat_history.append({"role": "assistant", "content": ai_output})

    # Log interaction to memory
    memory_log.append({
        "timestamp": datetime.now().isoformat(),
        "user": user_input,
        "sentiment": sentiment,
        "ai_response": ai_output,
        "brain_state": {k: v.value for k, v in brain.nodes.items()}
    })

    return ai_output

# --- Run the Interactive Session ---
def run_chat():
    brain = Brain(DNA(sex="male"))  # You can change sex to "female" or "neutral"
    memory_log = []
    chat_history = []

    print("Start chatting with your emotional AI. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        ai_response = chat_with_user(user_input, brain, memory_log, chat_history)
        print("AI:", ai_response)

    # Save memory log on exit
    filename = f"memory_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(memory_log, f, indent=2)
    print(f"Conversation saved to {filename}")

if __name__ == "__main__":
    run_chat()
