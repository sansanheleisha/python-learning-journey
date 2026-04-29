from utils import count_words, format_output

text = input("Enter a sentence: ")

if not text.strip():
    print("You entered an empty string")
else:
    count = count_words(text)
    print(format_output(count))
