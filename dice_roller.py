import random

def roll_dice(num_dice, sides):
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    return rolls

def show_menu():
    print("\nDice Roller")
    print("1. Roll a Single Die")
    print("2. Roll Multiple Dice")
    print("3. Exit")

while True:
    show_menu()
    choice = input("\nChoose an option (1-3): ")

    if choice == "1":
        sides = int(input("Enter the number of sides on the die (e.g., 6 for a standard die): "))
        result = roll_dice(1, sides)
        print(f"\nYou rolled: {result[0]}")
    elif choice == "2":
        sides = int(input("Enter the number of sides on the dice: "))
        num_dice = int(input("Enter the number of dice to roll: "))
        results = roll_dice(num_dice, sides)
        print(f"\nYou rolled: {', '.join(map(str, results))}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
