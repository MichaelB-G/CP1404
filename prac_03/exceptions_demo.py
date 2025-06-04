"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

  #1.When will a ValueError occur?
  # When I write a string in either the numerator or denominator,
  # "Numerator and denominator must be valid numbers!"
  # The program also finishes at this point, because it is not in a loop.

  #2.When will a ZeroDivisionError occur?
  # When "0" is entered when selecting a denominator, and again the program finishes.

  #3.Could you change the code to avoid the possibility of a ZeroDivisionError?
  # # Could you change the code to avoid the possibility of a ZeroDivisionError?
  # → Yes, instead of using a try-except block for ZeroDivisionError,
  #   you could add a while loop that keeps asking the user to enter a non-zero denominator.
  #   This would prevent the error from ever occurring by validating the input beforehand.

  # Example:
  # while denominator == 0:
  #     print("Denominator cannot be 0.")
  #     denominator = int(input("Enter the denominator: "))