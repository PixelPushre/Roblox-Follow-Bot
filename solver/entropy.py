import random

def generate_entropy():
    return sum(random.randint(1, 9999) for _ in range(100))
