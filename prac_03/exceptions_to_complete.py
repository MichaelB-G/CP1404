"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
number = 0  # this is to stop pycharm from complaining
while not is_finished:
    try:
        number = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:  # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", number)