"""Menu program to display score result and stars."""

def main():
    """Run the menu-based score program."""
    score = get_valid_score()
    choice = get_menu_choice()
    while choice != "Q":
        if choice == "P":
            print(determine_score_result(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        choice = get_menu_choice()
    print("Farewell.")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = float(input("Enter score (0-100): "))
    return score


def get_menu_choice():
    """Display menu and return the user's choice as uppercase."""
    print("\nMenu:\n(P)rint result\n(S)how stars\n(Q)uit")
    return input(">>> ").upper()


def determine_score_result(score):
    """Return the result category based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
