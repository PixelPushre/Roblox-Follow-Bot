import random
import string

def random_string(length=12):
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
