import random
import re

responses = {
    "i feel (.*)": ["Why do you feel }?", "How long have you been feeling {}?"],
    "i am (.*)": ["Why do you say you're {}?", "How long have you been {}?"],
    "i'm (.*)": ["Why are you {}?", "How long have you been {}?"],
    "i (.*) you": ["Why do you {} me?", "What makes you think you {} me?"]
}


print("Eliza: Hello, I'm Eliza. What's on your mind?")
input_text = input('You: ')

while input_text:
    matched = False
    for pattern, phrases in responses.items():
        match = re.match(pattern, input_text, re.IGNORECASE)
        if match:
            # Select a random response template and format it with the captured group
            response = random.choice(phrases).format(*match.groups())
            print("Eliza:", response)
            matched = True
            break
        else:
          print("Eliza: Can you explain the problem to me more closely?")

    input_text = input('You: ')