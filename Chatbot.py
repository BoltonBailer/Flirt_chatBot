import random

# Dictionary of flirty responses
flirty_responses = {
    "cute": ["Aww, stop it! You’re making me blush 😘", "You think so? Well, you're not so bad yourself 😉"],
    "handsome": ["Oh, you're making me smile! Tell me more 😏"],
    "beautiful": ["Flattery will get you everywhere! 😘"],
    "date": ["Are you asking me out? Because I might just say yes 😉"],
    "kiss": ["Hmm, let’s not get ahead of ourselves... or should we? 😘"],
    "love": ["Wow, I didn’t know we were moving this fast 😳❤️"],
    "hot": ["Ohh, is it me or is it getting hot in here? 🔥"],
    "sweetheart": ["You're making my AI circuits overheat! 🥰"]
}

# Function to get flirty response ADDDDED STUFF
def get_flirty_response(user_input):
    user_words = user_input.lower().split()
    
    for word in user_words:
        if word in flirty_responses:
            return random.choice(flirty_responses[word])  # Pick a random flirty response
    
    return random.choice([
        "Ooh, that’s interesting! Tell me more 😏",
        "I like where this is going… but you gotta be smoother than that 😉",
        "You’re cute when you try so hard to impress me 😘"
    ])

# Main chat loop
print("FlirtyBot 😘: Hey there, cutie! What’s on your mind?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("FlirtyBot 😘: Aww, leaving so soon? I'll miss you! 😘")
        break
    
    response = get_flirty_response(user_input)
    print(f"FlirtyBot 😘: {response}")
