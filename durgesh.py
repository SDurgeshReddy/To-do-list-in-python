import os

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines() if line.strip()]
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    new_task = input("Enter the task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{new_task}' added successfully!")

def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the index of the task to edit: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_index] = new_task
            save_tasks(tasks)
            print("Task edited successfully!")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Task '{deleted_task}' deleted successfully!")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== To-Do List =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()
