import random
import math

def useless_entropy():
    x = random.random()
    for _ in range(5000):
        x = math.sin(x) ** 2 + math.cos(x)
    return x
