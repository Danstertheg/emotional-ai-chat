# Emotional AI Chat

This is an experimental prototype that integrates a lightweight emotional simulation engine with GPT-4 to create a conversational AI that appears to evolve its mood, beliefs, and goals based on how it is treated by the user.

## 🔥 Features

* Emotion-driven GPT-4 responses using a dynamic "Brain" model
* Real-time sentiment classification via GPT-4
* Brain graph with hormone nodes (e.g., dopamine, cortisol, oxytocin)
* Persistent personality and emotional evolution across a single session
* Memory log saved to disk after every conversation

## 🧠 How It Works

1. User input is classified as **positive**, **negative**, or **neutral** using GPT-4
2. Sentiment is mapped to internal events (e.g., "failure" increases cortisol)
3. The brain updates emotional hormone levels using a graph-like propagation model
4. GPT-4 is prompted using emotional state + belief + current goal
5. Full conversation history is tracked to maintain multi-turn coherence
6. On exit, all memory and brain states are saved to a JSON file

## 💬 Example Prompt Sent to GPT-4

```
You are an emotionally evolving AI. You currently feel joy, your belief is 'I am capable of understanding others.', and your current goal is to build trust.
```

## 🛠️ Setup

```bash
pip install openai
```

Make sure you have your OpenAI API key set:

```bash
export OPENAI_API_KEY=your-key-here  # or set in .env file
```

You also need the companion `brain.py` module that defines the Brain, DNA, and emotion logic.

## 🚀 Run It

```bash
python emotional_ai_chat.py
```

## 📦 Output

At the end of your session, a file like `memory_log_20250716_213045.json` will be created with the emotional trace and full dialogue history.

## 📚 Future Directions

* Add long-term memory recall between sessions
* Allow belief rewiring based on emotional conditioning
* Visualize emotional state over time
* Support multi-emotion classification (e.g., admiration, disgust)
* Package as an emotional personality SDK for NPCs or AI companions

## 📜 License

MIT License (feel free to modify or extend)

---

> This project explores the emotional illusion in AI. It does not create sentient or self-aware agents — only the appearance of feeling. Use responsibly.
