"""
CP1404/CP5632 - Practical
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0.")
        denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(result)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
