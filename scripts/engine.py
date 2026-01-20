import time
import random
from scripts.logger import log
from solver.captcha_solver import solve_captcha
from utils.string_noise import random_string
from utils.junk_math import useless_entropy

def fake_delay(a=0.6, b=1.4):
    time.sleep(random.uniform(a, b))

def run_simulation(userid):
    print("\nInitializing session...\n")
    fake_delay()

    steps = [
        "Fetching proxy list",
        "Validating proxy rotation",
        "Creating virtual account container",
        "Generating browser fingerprint",
        "Injecting headers",
    ]

    for step in steps:
        print(f"[+] {step}...")
        useless_entropy()
        fake_delay()

    print("\n[~] Solving captcha...")
    solve_captcha()

    followers = random.randint(12, 47)
    print(f"\n[✓] Starting follow sequence ({followers} actions)\n")

    for i in range(followers):
        fake_delay(0.4, 1.2)
        print(f"[+] Attempting follow | session={random_string(8)}")
        fake_delay(0.2, 0.5)
        print(f"[✓] Followed user: {userid}")

    print("\n[✓] Task completed successfully")
    log(f"Simulated followers sent to {userid} | count={followers}")
