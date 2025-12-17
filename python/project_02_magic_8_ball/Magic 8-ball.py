import random

# 20 classic Magic 8-Ball responses
responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

print("🎱 Welcome to the Magic 8-Ball!")

while True:
    input("Ask me a yes/no question: ")
    answer = responses[random.randint(0, len(responses) - 1)]
    print("Magic 8-Ball says:", answer, "\n")
