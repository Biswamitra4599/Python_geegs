import json
import random

with open("intents.json") as file:
    data = json.load(file)

def chatbot_response(user_input):
    user_input = user_input.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."

print("Chatbot is running (type 'quit' to exit)")
while True:
    message = input("You: ")
    if message.lower() == "quit":
        break
    print("Bot:", chatbot_response(message))
