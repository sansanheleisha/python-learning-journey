from utils import count_words, format_output, log
from utils import save_history
save_history({"text": text, "count": count_words(text)})
def run():
    while True:
        print("\n1. Count words")
        print("2. Exit")
print("3. Show history")

        choice = input("Choose option: ")
        log(f"Choice: {choice}")

        if choice == "1":
            text = input("Enter text: ")
            if not text.strip():
                print("Empty input!")
            else:
                print(format_output(count_words(text)))

        elif choice == "2":
            break
elif choice == "3":
    with open("history.json", "r") as f:
        print(f.read())
