"""
CP1404/CP5632 Practical
Quick Picks - Random Lottery Generator
"""

import random

NUMBERS_PER_PICK = 6
MIN = 1
MAX = 45

def main():
    number_of_picks = int(input("How many quick picks? "))

    for _ in range(number_of_picks):
        pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in pick))


def generate_quick_pick():
    """Generate one quick pick (6 unique random numbers sorted)."""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN, MAX)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


main()
