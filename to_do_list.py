import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "r")
        tasks = file.read().splitlines()
        file.close()
    return tasks

# Save tasks to file
def save_tasks(tasks):
    file = open(FILE_NAME, "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nTasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print("Deleted:", removed)
            else:
                print("Invalid number!")

    # Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
        print("Invalid choice!")
