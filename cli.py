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

        print("\n==== HISTORY ====")

        for item in data:
            print(f'Text: "{item["text"]}" | Words: {item["count"]}')

    except FileNotFoundError:
        print("No history file found.")


def show_stats():
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            print("No statistics available.")
            return

        total_checks = len(data)

        total_words = 0

        for item in data:
            total_words += item["count"]

        average_words = total_words / total_checks

        print("\n==== STATISTICS ====")
        print(f"Total checks: {total_checks}")
        print(f"Total words counted: {total_words}")
        print(f"Average words per text: {average_words:.2f}")

    except FileNotFoundError:
        print("No statistics available.")


def clear_history():
    with open("history.json", "w", encoding="utf-8") as f:
        json.dump([], f)

    print("History cleared.")


def run():
    while True:
        print("\n==== MENU ====")
        print("1. Count words")
        print("2. Show history")
        print("3. Show statistics")
        print("4. Clear history")
        print("5. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            handle_count()

        elif choice == "2":
            show_history()

        elif choice == "3":
            show_stats()

        elif choice == "4":
            clear_history()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")
