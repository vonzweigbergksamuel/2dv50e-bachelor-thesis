import random


def generate_random_seed():
    """
    Generates a random state for the preprocess service.
    """
    return random.randint(0, 1000000)


def get_random_seeds(amount: int):
    seeds = []
    
    for i in range(amount):
        seed = generate_random_seed()
        
        seeds.append(seed)

    return seeds
        