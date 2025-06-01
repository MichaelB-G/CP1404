"""Get a score and print its category using a function."""

import random

def main():
    """Get user score, determine result, then do the same for a random score."""
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(f"Your score is: {result}")

    random_score = random.uniform(0, 100)
    random_result = determine_score_result(random_score)
    print(f"Random score: {random_score:.2f} is {random_result}")

def determine_score_result(score):
    """Return the result category based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
