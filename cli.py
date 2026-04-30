from utils import count_words, format_output, log, save_history
import json


def handle_count():
    text = input("Enter a sentence: ")

    if not text.strip():
        print("Empty input!")
        return

    count = count_words(text)
    result = format_output(count)

    print(result)

    log(f"Counted words: {text} -> {count}")
    save_history({"text": text, "count": count})


def show_history():
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            print("No history yet.")
            return

        for item in data:
            print(item)

    except FileNotFoundError:
        print("No history file found.")


def run():
    while True:
        print("\n==== MENU ====")
        print("1. Count words")
        print("2. Show history")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            handle_count()

        elif choice == "2":
            show_history()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")
