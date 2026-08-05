# Building a todo app using python
from __future__ import annotations

tasks: list[dict[str, object]] = []

def add_task(task_text: str) -> dict[str, object]:
    task_text = task_text.strip()
    task = {"task": task_text, "done": False}
    tasks.append(task)
    return task


def get_tasks() -> list[dict[str, object]]:
    return tasks.copy()


def mark_task_done(task_index: int) -> bool:
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["done"] = True
        return True
    return False


def delete_task(task_index: int) -> bool:
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        return True
    return False


def show_menu() -> None:
    print("\nTodo App Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def cli_add_task() -> None:
    task = input("Enter the task: ")
    if task.strip():
        add_task(task)
        print("Task added successfully!")
    else:
        print("Task was empty. Please enter a valid task.")


def view_tasks() -> None:
    tasks_list = get_tasks()
    if not tasks_list:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks_list, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']} {status}")


def cli_mark_done() -> None:
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to mark as done: "))
            if mark_task_done(task_num):
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def cli_delete_task() -> None:
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if delete_task(task_num):
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
            cli_add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            cli_mark_done()
        elif choice == '4':
            cli_delete_task()
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()  