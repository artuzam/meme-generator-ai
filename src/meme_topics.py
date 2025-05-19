import random


def get_random_topic():
    topics = [
        "dogs or cats",
        "dad jokes",
        "cringy office humor",
        "internet trends",
        "puns",
        "pop culture references",
        "relationship humor",
        "spongebob",
        "sports"
    ]
    
    return random.choice(topics)