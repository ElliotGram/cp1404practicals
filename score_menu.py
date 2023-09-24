import random

def main():
    print("Welcome to the Score Program!")
    choice = input("Enter your choice: ").strip().lower()
    score = handle_menu_choice(choice, score)

    while choice != 'q':
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").strip().lower()
        score = handle_menu_choice(choice, score)


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        return '*' * int(score)


def get_valid_score():
    score = 0
    while score == 0:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if not 0 <= score <= 100:
                print("Invalid score. Please enter a score between 0 and 100.")
                score = None
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return score


def handle_menu_choice(choice, score):
    if choice == 'g':
        score = get_valid_score()
    elif choice == 'p':
        if score is not None:
            result = determine_result(score)
            print(f"Result: {result}")
        else:
            print("Please get a valid score first.")
    elif choice == 's':
        if score is not None:
            stars = print_stars(score)
            print(f"Stars: {stars}")
        else:
            print("Please get a valid score first.")
    elif choice == 'q':
        print("Thank you for using the Score Program. Goodbye!")
    else:
        print("Invalid choice. Please choose a valid option.")

    return score



main()
