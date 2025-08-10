"""
Wimbledon Winners
Estimate: 1 hour
Actual: 2 hours
"""

FILENAME = "wimbledon.csv"


def main():
    data = read_wimbledon_data(FILENAME)
    champion_to_wins, countries = process_data(data)
    display_champions(champion_to_wins)
    display_countries(countries)


def read_wimbledon_data(filename):
    """Read Wimbledon CSV file and return data rows (excluding header)."""
    with open(filename, encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        lines = [line.strip().split(',') for line in in_file]
    return lines


def process_data(data):
    """Return dict of champions to win counts and set of countries."""
    champion_to_wins = {}
    countries = set()
    for row in data:
        champion = row[2]
        country = row[1]
        countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins, countries


def display_champions(champion_to_wins):
    """Display champions and their win counts."""
    print("Wimbledon Champions:")
    for name, wins in sorted(champion_to_wins.items()):
        print(f"{name} {wins}")


def display_countries(countries):
    """Display all countries with champions, sorted alphabetically."""
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
