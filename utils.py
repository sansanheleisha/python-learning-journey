def count_words(text):
    """Return the number of words in the given text."""
    return len(text.split())


def format_output(count):
    """Return formatted string with word count."""
    return f"Total words: {count}"

def log(message):
    with open("app.log", "a") as f:
        f.write(message + "\n")

import json

def save_history(entry):
    try:
        with open("history.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open("history.json", "w") as f:
        json.dump(data, f, indent=2)
