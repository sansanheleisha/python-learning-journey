import json


def count_words(text):
    """Return the number of words in the given text."""
    return len(text.split())


def format_output(count):
    """Return formatted string with word count."""
    return f"Total words: {count}"


def log(message):
    with open("app.log", "a", encoding="utf-8") as f:
        f.write(message + "\n")


def save_history(entry):
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open("history.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
