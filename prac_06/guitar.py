class Guitar:
    """Represent a guitar."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is."""
        return 2022 - self.year  # You can update this later to be dynamic if you want

    def is_vintage(self):
        """Return True if the guitar is vintage (50 or more years old)."""
        return self.get_age() >= 50
