"""
CP1404/CP5632 - Practical
File operations exercises:
1. Write user's name to a file
2. Read the name back and greet the user
3. Read and sum the first two numbers from a file
4. Read all numbers from a file and calculate the total
Demonstrates use of open/close, with statements, and different file reading methods.
"""

# Task 1 - Write user's name to a file
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Task 2 - Read the name from name.txt and greet the user
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hello, {name}!")

#practice creating files
with open("numbers.txt", "w") as out_file:
    out_file.write("17\n")
    out_file.write("42\n")
    out_file.write("400\n")

# Task 3 - Read the first two numbers and print their sum
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    total = first_number + second_number
print(total)

# Task 4 - Read all numbers in numbers.txt and print their total
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)


