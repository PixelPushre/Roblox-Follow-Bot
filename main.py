import time
from scripts.ui import show_banner, main_menu
from scripts.engine import run_simulation

def main():
    show_banner()
    choice = main_menu()

    if choice == "1":
        target = input("\nPaste Roblox UserID: ").strip()
        if not target.isdigit():
            print("Invalid UserID format.")
            return
        run_simulation(target)
    else:
        print("Exiting...")
        time.sleep(1)

if __name__ == "__main__":
    main()
