from datetime import datetime

def log(text):
    with open("output/sessions.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {text}\n")
