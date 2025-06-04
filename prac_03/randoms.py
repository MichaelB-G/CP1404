"""
CP1404/CP5632 - Practical
Randoms - Using the random module and analysing output ranges
"""
import random

print(random.randint(5, 20))
print(random.randrange(3, 10, 2))
print(random.uniform(2.5, 5.5))

# Line 1
# Smallest = 5, Largest = 20
# Example values: 5, 11, 20

# Line 2
# Smallest = 3, Largest = 9
# Values must be 3, 5, 7, or 9
# Could it be 4? No because it starts at 3 and increments by 3

# Line 3
# Smallest = 2.5, Largest = 5.5
# Example values: 2.78, 3.14, 5.49


print(random.randint(1, 100))
# Random number between 1 and 100 inclusive


