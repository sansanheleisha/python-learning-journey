from utils import count_words, format_output, log

def run():
    while True:
        print("\n1. Count words")
        print("2. Exit")

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
