def reverse_string(text):
    return text[::-1]


if __name__ == "__main__":
    user_input = input("Enter text: ")
    print("Reversed:", reverse_string(user_input))
