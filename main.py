from utils import count_words

text = input("Enter a sentence: ")
print("Word count:", count_words(text))

from utils import count_words

text = input("Enter a sentence: ")

if not text.strip():
    print("You entered an empty string")
else:
    print("Word count:", count_words(text))
