"""
Emails
Estimate: 15 minutes
Actual: <fill this in>
"""

email_to_name = {}

email = input("Email: ")
while email != "":
    # Preserve email exactly as typed by the user
    name_guess = email.split('@')[0].replace('.', ' ').title()
    confirmation = input(f"Is your name {name_guess}? (Y/n) ").lower()
    if confirmation != "" and confirmation != "y":
        name = input("Name: ")
    else:
        name = name_guess
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
