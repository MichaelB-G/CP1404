"""
CP1404 Practical 09 - Taxi Simulator
Simulates driving taxis and accumulating fares.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Run the taxi simulator program."""
    print("Let's drive!")
    bill = 0.0
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None

    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                bill += drive_taxi(current_taxi)
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    list_taxis(taxis)


def choose_taxi(taxis):
    """Allow the user to choose a taxi from the list."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    try:
        choice = int(input("Choose taxi: "))
        return taxis[choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


def drive_taxi(taxi):
    """Drive the chosen taxi and return fare cost."""
    taxi.start_fare()
    distance = float(input("Drive how far? "))
    taxi.drive(distance)
    fare = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${fare:.2f}")
    return fare


def list_taxis(taxis):
    """Display all taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
