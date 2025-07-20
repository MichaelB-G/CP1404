from project import Project
import datetime

FILENAME = "projects.txt"


def main():
    """Main menu-driven project management program."""
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = (
        "- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit"
    )

    print("Welcome to Pythonic Project Management")

    choice = input(menu + "\n>>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice")
        choice = input(menu + "\n>>> ")

    save_prompt = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_prompt in ('y', 'yes'):
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # skip header
        for line in file:
            parts = line.strip().split('\t')
            projects.append(Project(*parts))
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display projects grouped by completion."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects: ")
    for p in sorted(incomplete):
        print(f"  {p}")
    print("Completed projects: ")
    for p in sorted(complete):
        print(f"  {p}")


def filter_projects_by_date(projects):
    """Filter and display projects starting after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.starts_after(filter_date)]
    for p in sorted(filtered, key=lambda p: p.start_date):
        print(p)


def add_project(projects):
    """Prompt for project details and add to list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))


def update_project(projects):
    """Let user choose a project and update its completion and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    project = projects[index]
    print(project)
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)
    if new_priority:
        project.priority = int(new_priority)


if __name__ == '__main__':
    main()
