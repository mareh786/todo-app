# Building a todo app using python
tasks = []
def show_menu():
    print("\nTodo App Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']}{status}")

def mark_done():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["done"] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                del tasks[task_num - 1]
                print("Task deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()  