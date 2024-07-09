import random

def lambda_handler(event, context): 
    random_film = random.choice([
    "Inception",
    "The Matrix",
    "Interstellar",
    "Pulp Fiction",
    "The Godfather",
    "Forrest Gump",
    "The Shawshank Redemption",
    "Fight Club",
    "The Dark Knight",
    "Gladiator"
])
    return random_film