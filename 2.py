location = "home"

while True:
    print("\n")

    # --- STATE 1: HOME ---
    if location == "home":
        print("You are at HOME.")
        choice = input("Where to go? (school / store / quit): ")

        if choice == "school":
            location = "school"
        elif choice == "store":
            location = "store"
        elif choice == "quit":
            print("\nThanks for playing! Goodbye.")
            break  # <--- Stops the 'while True:' loop!
        else:
            print("Invalid choice! You stay at home.")

    # --- STATE 2: SCHOOL ---
    elif location == "school":
        print("You are at SCHOOL studying.")
        choice = input("Where to go? (home / park): ")

        if choice == "home":
            location = "home"
        elif choice == "park":
            location = "park"
        else:
            print("Invalid choice! You stay at school.")

    # --- STATE 3: PARK ---
    elif location == "park":
        print("You are at the PARK relaxing.")
        choice = input("Where to go? (home / store): ")

        if choice == "home":
            location = "home"
        elif choice == "store":
            location = "store"
        else:
            print("Invalid choice! You stay at the park.")

    # --- STATE 4: STORE ---
    elif location == "store":
        print("You are at the STORE buying snacks.")
        choice = input("Where to go? (home / park): ")

        if choice == "home":
            location = "home"
        elif choice == "park":
            location = "park"
        else:
            print("Invalid choice! You stay at the store.")

