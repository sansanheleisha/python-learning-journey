from utils import count_words, format_output, log, save_history
import json


def handle_count():
   if len(text) > 200:
    print("Text is too long. Maximum 200 characters.")
    return

    if not text.strip():
        print("Empty input!")
        return

    count = count_words(text)
    result = format_output(count)

    print(result)

    log(f"Counted words: {text} -> {count}")
    save_history({"text": text, "count": count})


def load_history():
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            return json.load(f)

except (FileNotFoundError, json.JSONDecodeError):
    return []


def show_history():
    data = load_history()

    if not data:
        print("No history yet.")
        return

    print("\n==== HISTORY ====")

    for item in data:
    print(
    f'Text: "{item["text"]}" | '
    f'Words: {item["count"]} | '
    f'Time: {item["timestamp"]}'
)


def search_history():
    keyword = input("Enter keyword: ").lower()

    data = load_history()

    found = False

    for item in data:
        if keyword in item["text"].lower():
            print(f'Found: "{item["text"]}"')
            found = True

    if not found:
        print("Nothing found.")


def show_stats():
    data = load_history()

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


def clear_history():
    with open("history.json", "w", encoding="utf-8") as f:
        json.dump([], f)

    print("History cleared.")


def export_history():
    data = load_history()

    if not data:
        print("No history to export.")
        return

    with open("history_export.txt", "w", encoding="utf-8") as f:
        for item in data:
         line = (
    f'Text: "{item["text"]}" | '
    f'Words: {item["count"]} | '
    f'Time: {item["timestamp"]}\n'
)
            f.write(line)

    print("History exported to history_export.txt")


def run():
    while True:
        print("\n==== MENU ====")
        print("1. Count words")
        print("2. Show history")
        print("3. Search history")
        print("4. Show statistics")
        print("5. Clear history")
        print("6. Export history")
        print("7. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            handle_count()

        elif choice == "2":
            show_history()

        elif choice == "3":
            search_history()

        elif choice == "4":
            show_stats()

        elif choice == "5":
            clear_history()

        elif choice == "6":
            export_history()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")
