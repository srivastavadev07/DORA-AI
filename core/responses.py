import random

thinking_responses = [
    "Thinking...",
    "Let me check.",
    "One moment.",
    "Looking that up.",
    "Give me a second.",
    "Analyzing your question.",
    "Let me think about that.",
]


def get_thinking_response():
    return random.choice(thinking_responses)