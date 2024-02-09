class ToDoApp:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("1. Add task")
        print("2. View tasks")
        print("3. Quit")

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

# Initialize the ToDoApp
todo_app = ToDoApp()

# Main loop
while True:
    todo_app.display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_app.add_task(task)
    elif choice == "2":
        todo_app.view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
