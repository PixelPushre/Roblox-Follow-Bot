import time
import random

def solve_captcha():
    stages = [
        "Downloading challenge data",
        "Analyzing patterns",
        "Applying entropy solver",
        "Bypassing visual layer",
        "Verifying token"
    ]

    for s in stages:
        print(f"    {s}...")
        time.sleep(random.uniform(0.6, 1.4))

    print("    Captcha solved ✓")
