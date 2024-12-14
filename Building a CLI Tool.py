import argparse
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the tasks file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the tasks file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """Add a new task to the list."""
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task['description']}")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if tasks:
        for task in tasks:
            print(f"{task['id']}. {task['description']}")
    else:
        print("No tasks found.")

def update_task(task_id, new_description):
    """Update the description of an existing task."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks(tasks)
            print(f"Task {task_id} updated to: {new_description}")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted.")
            return
    print(f"Task with ID {task_id} not found.")

def main():
    """Main function to parse arguments and call appropriate functions."""
    parser = argparse.ArgumentParser(description="A simple To-Do List CLI tool.")
    
    # Define commands and arguments
    subparsers = parser.add_subparsers(dest="command")
    
    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")
    
    # List tasks
    subparsers.add_parser("list", help="List all tasks")
    
    # Update task
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("task_id", type=int, help="ID of the task to update")
    update_parser.add_argument("new_description", help="New description of the task")
    
    # Delete task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Execute based on the command
    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "update":
        update_task(args.task_id, args.new_description)
    elif args.command == "delete":
        delete_task(args.task_id)
    else:
        print("Invalid command. Use --help for usage.")

if __name__ == "__main__":
    main()
