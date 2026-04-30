from utils import count_words, format_output

def main():
    while True:
        print("\n1. Count words")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            text = input("Enter a sentence: ")
            if not text.strip():
                print("Empty input!")
            else:
                count = count_words(text)
                print(format_output(count))

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

from utils import log
log(f"User selected option: {choice}")

from cli import run

if __name__ == "__main__":
    run()
try:
    text = input("Enter text: ")
except Exception as e:
    print("Error:", e)
