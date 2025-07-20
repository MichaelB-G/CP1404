import datetime


class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion %."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Sort projects by priority (lower number = higher priority)."""
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def starts_after(self, date):
        """Return True if project starts after the given date."""
        return self.start_date > date
