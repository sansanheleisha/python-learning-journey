def count_words(text):
    return len(text.split())


def format_output(count):
    return f"Total words: {count}"

def log(message):
    with open("app.log", "a") as f:
        f.write(message + "\n")
