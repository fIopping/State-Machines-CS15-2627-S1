place = "computer class"
while True:
    print(f"\n")
    if place == "computer class":
        print(f"Your on a computer\n")
        choice = input("Would you (play a game/do assignment/Snapchat) ").lower
        if choice == "play a game":
            place = "game"
        elif choice == "do assignment":
            place = "assignment"
        elif choice == "Snapchat":
            place = "snapchat"
        else:
            print("Type one of the choices ;-;")

    if place == "game":
        print(f"Your on a game\n")
        choice = input("You died (do assignment/Snapchat) ").lower()
        if choice == "do assignment":
            place = "assignment"
        elif choice == "Snapchat":
            place = "snapchat"
        else:
            print("Type one of the choices ;-;")

    if place == "assignment":
        print(f"Your bored\n")
        choice = input("Would you (Snapchat) ").lower()
        if choice == "Snapchat":
            place = "snapchat"
        else:
            print("Type one of the choices ;-;")



