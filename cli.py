def run():
    while True:
        print("\n==== MENU ====")
        print("1. Count words")
        print("2. Show history")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            handle_count()

        elif choice == "2":
            show_history()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")
