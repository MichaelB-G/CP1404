from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load, display, extend, sort and save guitars."""
    guitars = load_guitars(FILENAME)

    print("These are the current guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.extend(get_new_guitars())

    guitars.sort(key=lambda g: g.year)

    print("\nThese are the sorted guitars:")
    for guitar in guitars:
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"{guitar}{vintage}")

    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Read guitars from a CSV file into Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def get_new_guitars():
    """Prompt user to enter new guitars."""
    new_guitars = []
    print("\nAdd new guitars:")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Save the list of guitars back to the file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
