import random

def lambda_handler(event, context): 
    random_quote = random.choice([
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do not watch the clock. Do what it does. Keep going.",
    "Keep your face always toward the sunshine—and shadows will fall behind you.",
    "The future belongs to those who believe in the beauty of their dreams."
])
    return random_quote