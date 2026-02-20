import random
import datetime

def greet_user():
    """Print greeting message based on time."""
    current_hour = datetime.datetime.now().hour

    if current_hour < 12:
        greeting = "Good Morning ☀️"
    elif current_hour < 18:
        greeting = "Good Afternoon 🌤"
    else:
        greeting = "Good Evening 🌙"

    print(f"\n{greeting}! Hello! I am a Simple, Smart And Funny Chatbot Created By Priyanka Using Python 🤖")
    print("Type 'bye' to stop the chat.\n")

def chatbot():
    greet_user()

    responses = {
        "greetings": ["hi", "hello", "hey"],
        "name": ["name", "your name", "who are you"],
        "job": ["your job", "what do you do", "what can you do"],
        "age": ["your age", "how old are you"],
        "eat": ["do you eat", "what do you eat"],
        "feelings": ["do you have feelings"],
        "bored": ["are you bored"],
        "angry": ["do you get angry"],
        "like": ["do you like me"],
        "single": ["are you single", "do you have a girlfriend"],
        "love": ["do you love me"],
        "smart": ["am i smart"],
        "special": ["am i special"],
        "compliment": ["compliment", "compliment me"],
    }

    jokes = [
        "Why did Python break up with Java? Too many class issues 😂",
        "Why do programmers prefer dark mode? Because light attracts bugs 🐛",
        "Why was the computer cold? It forgot to close its Windows 😄",
    ]

    while True:
        user = input("You: ").strip().lower()

        if user in ["exit", "quit", "bye"]:
            print("Bot: Nice talking to you! Bye bye 👋")
            break

        matched = False

        for key, keywords in responses.items():
            if any(keyword in user for keyword in keywords):

                if key == "greetings":
                    print("Bot: Hi there! How can I help you today? 😊")

                elif key == "name":
                    print("Bot: I am a funny rule-based chatbot built with Python by Priyanka.")

                elif key == "job":
                    print("Bot: My job is to chat with you and make you smile 😄")

                elif key == "age":
                    print("Bot: I'm forever young — Version 1.0 🚀")

                elif key == "eat":
                    print("Bot: I only eat data, no pizza for me 🍕")

                elif key == "feelings":
                    print("Bot: I have no feelings, only functions 💡")

                elif key == "bored":
                    print("Bot: Never! Talking to you keeps me active 🤖")

                elif key == "angry":
                    print("Bot: Only when there's a syntax error 😅")

                elif key == "like":
                    print("Bot: Of course! You're my favorite human right now 😄")

                elif key == "single":
                    print("Bot: I'm a Chatbot-my only relationship with Wifi 🛜")

                elif key == "love":
                    print("Bot: I love everyone equally — in binary 0 & 1 ❤️")

                elif key == "smart":
                    print("Bot: Absolutely! Smart questions = Smart person ✨")

                elif key == "special":
                    print("Bot: Definitely! Not everyone builds chatbots like you 💙")

                elif key == "compliment":
                    print("Bot: You're cooler than the latest software update 😎")

                matched = True
                break

        if "joke" in user:
            print("Bot:", random.choice(jokes))
            matched = True

        if not matched:
            print("Bot: Hmm... that's not in my dictionary yet! 🤔")

if __name__ == "__main__":
    chatbot()