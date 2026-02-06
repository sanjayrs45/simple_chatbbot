print("Bot: Hello! I am a smart chatbot 🤖")
print("Bot: Type 'bye' to exit 👋")

responses = {
    "hi": "Hello 👋",
    "hello": "Hi there 😊",
    "thanks": "Welcome 😄",
    "good morning": "Good morning ☀️",
    "good night": "Good night 🌙",
    "bye": "Bye! See you soon 👋"
}

while True:
    user = input("You: ").lower()

    if user in responses:
        print("Bot:", responses[user])
        if user == "bye":
            break
    else:
        print("Bot: Sorry, I don't understand 😅")
