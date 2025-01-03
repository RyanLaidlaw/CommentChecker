class ToDoList:
    """Class to manage a simple to-do list."""

    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []

    def add_task(self, task):
        """Add a task to the to-do list.

        Args:
            task (str): The task description.
        """
        if task:
            self.tasks.append(task)  # Add task if it's not empty
            print(f"Task added: {task}")
        else:
            print("Task cannot be empty.")

    def remove_task(self, index):
        """Remove a task by its index.

        Args:
            index (int): The position of the task to remove.
        """
        try:
            removed = self.tasks.pop(index)  # Attempt to remove the task
            print(f"Task removed: {removed}")
        except IndexError:
            print("Invalid task index.")  # Handle invalid indices

    def display_tasks(self):
        """Display all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                # Display each task with its index for reference
                print(f"{i}: {task}")

# Main block to demonstrate the usage of ToDoList
if __name__ == "__main__":
    # Create an instance of ToDoList
    todo = ToDoList()

    # Add some tasks
    todo.add_task("Buy groceries")
    todo.add_task("Read a book")
    todo.add_task("Exercise for 30 minutes")

    # Display current tasks
    todo.display_tasks()

    # Remove a task and display tasks again
    todo.remove_task(1)  # Removes the task at index 1
    todo.display_tasks()

    # Attempt to remove a task with an invalid index
    todo.remove_task(10)
