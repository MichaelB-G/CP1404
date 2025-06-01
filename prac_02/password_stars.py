MIN_LENGTH = 6

def main():
    """Get a valid password and print asterisks the same length as the password."""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get a valid password with a minimum length."""
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters.")
        password = input("Enter password: ")
    return password

def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))


main()
