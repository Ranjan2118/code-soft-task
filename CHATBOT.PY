import random
import re

# Define rules and responses
rules = {
    r'hello|hi|hey': ['Hello!', 'Hey there!', 'Hi!'],
    r'how are you|how are you doing': ["I'm good, thank you!", "I'm doing well, how about you?"],
    r'what can you do|help': ["I can chat with you! Ask me anything.", "I'm here to chat with you."],
    r'bye|goodbye': ["Goodbye!", "Bye! Have a great day!"],
    r'(.*) age\??': ["I don't have an age, I'm just a computer program!"],
    r'(.*) (name|call you) (.*)': ["You can call me Chatbot."],
    r'(.*) (weather|temperature) (.*)': ["I'm sorry, I don't have access to weather information."],
    r'(.*)': ["I'm sorry, I'm not sure I understand.", "Could you please clarify?"]
}

def respond(message):
    for pattern, responses in rules.items():
        if re.search(pattern, message, re.IGNORECASE):
            return random.choice(responses)
    return random.choice(rules[r'(.*)'])  # Default response if no pattern matches

# Main interaction loop
print("Hello! I'm Chatbot. Ask me anything or say 'bye' to exit.")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'bye':
        print(respond(user_input))
        break
    else:
        response = respond(user_input)
        print("Chatbot:", response)
