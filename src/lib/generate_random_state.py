import random


def generate_random_state():
    """
    Generates a random state for the preprocess service.
    """
    return random.randint(0, 1000000)
