"""
Todo application CLI interface.
"""
from todo import TodoList, Task, Priority


def display_menu():
    """
    Show the main menu options to the user.
    """
    print("\nTodo Application")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Mark task as complete/incomplete")
    print("6. Assign priority to task")
    print("7. Add tags to task")
    print("8. Remove tags from task")
    print("9. Search tasks")
    print("10. Filter tasks")
    print("11. Sort tasks")
    print("12. Exit")


def get_task_status_indicator(task: Task) -> str:
    """
    Get the status indicator for a task.

    Args:
        task: The task to get status for

    Returns:
        String representation of the task's completion status
    """
    return "[x]" if task.completed else "[ ]"


def format_task_display(task: Task) -> str:
    """
    Format a task for display.

    Args:
        task: The task to format

    Returns:
        Formatted string representation of the task
    """
    status = get_task_status_indicator(task)

    # Get priority indicator
    priority_indicator = ""
    if task.priority == Priority.HIGH:
        priority_indicator = "[H]"
    elif task.priority == Priority.MEDIUM:
        priority_indicator = "[M]"
    elif task.priority == Priority.LOW:
        priority_indicator = "[L]"
    else:
        priority_indicator = "   "  # Three spaces for no priority

    # Format tags
    tags_display = ""
    if task.tags:
        tags_display = " " + " ".join([f"#{tag}" for tag in task.tags])

    return f"{task.id:2d} {priority_indicator} {status} {task.title:<20} {task.description}{tags_display}"


def main():
    """
    Main application loop with menu-driven interface.
    """
    todo_list = TodoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ").strip()

        if choice == "1":
            # Add a new task
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()

            task_id = todo_list.add_task(title, description)
            if task_id == -1:
                print("Error: Task title cannot be empty. Please provide a valid title.")
            else:
                print(f"Task '{title}' added successfully with ID: {task_id}")

        elif choice == "2":
            # View tasks with optional filters and sorting
            print("\nView options:")
            filter_choice = input("Apply filters? (y/n): ").strip().lower()

            if filter_choice in ['y', 'yes']:
                print("\nFilter options:")
                print("1. By status (completed/pending)")
                print("2. By priority (high/medium/low)")
                print("3. By tag")
                print("4. Combined filters")

                filter_choice = input("Choose filter type (1-4): ").strip()

                if filter_choice == "1":
                    status_input = input("Filter by status (completed/pending): ").strip().lower()
                    if status_input in ['completed', 'done', 'finished']:
                        status = True
                    elif status_input in ['pending', 'incomplete', 'todo']:
                        status = False
                    else:
                        print("Invalid status. Please use 'completed' or 'pending'.")
                        continue

                    tasks = todo_list.filter_tasks(status=status)

                elif filter_choice == "2":
                    priority_input = input("Filter by priority (high/medium/low): ").strip().lower()
                    if priority_input == "high":
                        priority = Priority.HIGH
                    elif priority_input == "medium":
                        priority = Priority.MEDIUM
                    elif priority_input == "low":
                        priority = Priority.LOW
                    else:
                        print("Invalid priority. Please use 'high', 'medium', or 'low'.")
                        continue

                    tasks = todo_list.filter_tasks(priority=priority)

                elif filter_choice == "3":
                    tag_input = input("Filter by tag: ").strip()
                    if not tag_input:
                        print("No tag provided. Please enter a valid tag.")
                        continue

                    tasks = todo_list.filter_tasks(tags=[tag_input])

                elif filter_choice == "4":
                    # Combined filters
                    status = None
                    priority = None
                    tags = []

                    status_input = input("Filter by status (completed/pending) or press Enter to skip: ").strip().lower()
                    if status_input:
                        if status_input in ['completed', 'done', 'finished']:
                            status = True
                        elif status_input in ['pending', 'incomplete', 'todo']:
                            status = False
                        else:
                            print("Invalid status. Please use 'completed' or 'pending'.")
                            continue

                    priority_input = input("Filter by priority (high/medium/low) or press Enter to skip: ").strip().lower()
                    if priority_input:
                        if priority_input == "high":
                            priority = Priority.HIGH
                        elif priority_input == "medium":
                            priority = Priority.MEDIUM
                        elif priority_input == "low":
                            priority = Priority.LOW
                        else:
                            print("Invalid priority. Please use 'high', 'medium', or 'low'.")
                            continue

                    tag_input = input("Filter by tag or press Enter to skip: ").strip()
                    if tag_input:
                        tags = [tag_input]

                    tasks = todo_list.filter_tasks(status=status, priority=priority, tags=tags)

                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")
                    continue
            else:
                # No filters - show all tasks
                tasks = todo_list.get_all_tasks()

            # Ask if user wants to sort the results
            sort_choice = input("Apply sorting? (y/n): ").strip().lower()
            if sort_choice in ['y', 'yes']:
                print("\nSort options:")
                print("1. By priority (High → Low)")
                print("2. By title (Alphabetical)")
                print("3. By status (Completed first)")

                sort_choice = input("Choose sort type (1-3): ").strip()

                if sort_choice == "1":
                    sort_by = "priority"
                elif sort_choice == "2":
                    sort_by = "title"
                elif sort_choice == "3":
                    sort_by = "status"
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    continue

                tasks = todo_list.get_sorted_tasks(tasks, sort_by=sort_by)

            # Display the tasks
            if not tasks:
                print("\nNo tasks match the specified filters.")
            else:
                print(f"\nShowing {len(tasks)} task(s):")
                print("\nID Pri Status Title               Description Tags")
                for task in tasks:
                    print(format_task_display(task))

        elif choice == "3":
            # Update a task
            try:
                task_id = int(input("Enter task ID to update: "))
                task = todo_list.get_task_by_id(task_id)
                if task is None:
                    print(f"Task with ID {task_id} not found. Please check the ID and try again.")
                    continue

                new_title = input(f"Enter new title (current: '{task.title}'): ").strip()
                new_description = input(f"Enter new description (current: '{task.description}'): ").strip()

                # If user presses Enter without typing anything, keep the current value
                if not new_title:
                    new_title = task.title
                if not new_description:
                    new_description = task.description

                success = todo_list.update_task(task_id, new_title, new_description)
                if success:
                    print(f"Task {task_id} updated successfully.")
                else:
                    print(f"Failed to update task {task_id}.")
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "4":
            # Delete a task
            try:
                task_id = int(input("Enter task ID to delete: "))
                success = todo_list.delete_task(task_id)
                if success:
                    print(f"Task {task_id} deleted successfully.")
                else:
                    print(f"Task with ID {task_id} not found. Please check the ID and try again.")
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "5":
            # Mark task as complete/incomplete
            try:
                task_id = int(input("Enter task ID to mark: "))
                task = todo_list.get_task_by_id(task_id)
                if task is None:
                    print(f"Task with ID {task_id} not found. Please check the ID and try again.")
                    continue

                current_status = "complete" if task.completed else "incomplete"
                new_status = input(f"Mark as complete? (current: {current_status}) [y/n]: ").strip().lower()

                if new_status in ['y', 'yes', '1', 'true']:
                    completed = True
                elif new_status in ['n', 'no', '0', 'false']:
                    completed = False
                else:
                    print("Invalid input. Please enter 'y' for complete or 'n' for incomplete.")
                    continue

                success = todo_list.mark_task_completed(task_id, completed)
                if success:
                    status = "complete" if completed else "incomplete"
                    print(f"Task {task_id} marked as {status}.")
                else:
                    print(f"Failed to mark task {task_id}.")
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "6":
            # Assign priority to task
            try:
                task_id = int(input("Enter task ID to assign priority: "))
                task = todo_list.get_task_by_id(task_id)
                if task is None:
                    print(f"Task with ID {task_id} not found. Please check the ID and try again.")
                    continue

                priority_input = input("Enter priority (high/medium/low): ").strip().lower()
                if priority_input == "high":
                    priority = Priority.HIGH
                elif priority_input == "medium":
                    priority = Priority.MEDIUM
                elif priority_input == "low":
                    priority = Priority.LOW
                else:
                    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
                    continue

                success = todo_list.assign_priority(task_id, priority)
                if success:
                    print(f"Priority '{priority_input}' assigned to task {task_id} successfully.")
                else:
                    print(f"Failed to assign priority to task {task_id}.")
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "7":
            # Add tags to task
            try:
                task_id = int(input("Enter task ID to add tags: "))
                task = todo_list.get_task_by_id(task_id)
                if task is None:
                    print(f"Task with ID {task_id} not found. Please check the ID and try again.")
                    continue

                tags_input = input("Enter tags to add (comma-separated): ").strip()
                if not tags_input:
                    print("No tags provided. Please enter at least one tag.")
                    continue

                tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
                if not tags:
                    print("No valid tags provided. Please enter at least one valid tag.")
                    continue

                success = todo_list.add_tags(task_id, tags)
                if success:
                    print(f"Tags {', '.join(tags)} added to task {task_id} successfully.")
                else:
                    print(f"Failed to add tags to task {task_id}.")
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "8":
            # Remove tags from task
            try:
                task_id = int(input("Enter task ID to remove tags: "))
                task = todo_list.get_task_by_id(task_id)
                if task is None:
                    print(f"Task with ID {task_id} not found. Please check the ID and try again.")
                    continue

                tags_input = input("Enter tags to remove (comma-separated): ").strip()
                if not tags_input:
                    print("No tags provided. Please enter at least one tag to remove.")
                    continue

                tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
                if not tags:
                    print("No valid tags provided. Please enter at least one valid tag to remove.")
                    continue

                success = todo_list.remove_tags(task_id, tags)
                if success:
                    print(f"Tags {', '.join(tags)} removed from task {task_id} successfully.")
                else:
                    print(f"Failed to remove tags from task {task_id}.")
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "9":
            # Search tasks
            keyword = input("Enter keyword to search: ").strip()
            if not keyword:
                print("No keyword provided. Please enter a keyword to search for.")
                continue

            matching_tasks = todo_list.search_tasks(keyword)
            if not matching_tasks:
                print(f"No tasks found containing '{keyword}'. Try a different search term.")
            else:
                print(f"\nFound {len(matching_tasks)} task(s) containing '{keyword}':")
                print("\nID Pri Status Title               Description Tags")
                for task in matching_tasks:
                    print(format_task_display(task))

        elif choice == "10":
            # Filter tasks
            print("\nFilter options:")
            print("1. By status (completed/pending)")
            print("2. By priority (high/medium/low)")
            print("3. By tag")
            print("4. Combined filters")

            filter_choice = input("Choose filter type (1-4): ").strip()

            if filter_choice == "1":
                status_input = input("Filter by status (completed/pending): ").strip().lower()
                if status_input in ['completed', 'done', 'finished']:
                    status = True
                elif status_input in ['pending', 'incomplete', 'todo']:
                    status = False
                else:
                    print("Invalid status. Please use 'completed' or 'pending'.")
                    continue

                filtered_tasks = todo_list.filter_tasks(status=status)

            elif filter_choice == "2":
                priority_input = input("Filter by priority (high/medium/low): ").strip().lower()
                if priority_input == "high":
                    priority = Priority.HIGH
                elif priority_input == "medium":
                    priority = Priority.MEDIUM
                elif priority_input == "low":
                    priority = Priority.LOW
                else:
                    print("Invalid priority. Please use 'high', 'medium', or 'low'.")
                    continue

                filtered_tasks = todo_list.filter_tasks(priority=priority)

            elif filter_choice == "3":
                tag_input = input("Filter by tag: ").strip()
                if not tag_input:
                    print("No tag provided. Please enter a valid tag.")
                    continue

                filtered_tasks = todo_list.filter_tasks(tags=[tag_input])

            elif filter_choice == "4":
                # Combined filters
                status = None
                priority = None
                tags = []

                status_input = input("Filter by status (completed/pending) or press Enter to skip: ").strip().lower()
                if status_input:
                    if status_input in ['completed', 'done', 'finished']:
                        status = True
                    elif status_input in ['pending', 'incomplete', 'todo']:
                        status = False
                    else:
                        print("Invalid status. Please use 'completed' or 'pending'.")
                        continue

                priority_input = input("Filter by priority (high/medium/low) or press Enter to skip: ").strip().lower()
                if priority_input:
                    if priority_input == "high":
                        priority = Priority.HIGH
                    elif priority_input == "medium":
                        priority = Priority.MEDIUM
                    elif priority_input == "low":
                        priority = Priority.LOW
                    else:
                        print("Invalid priority. Please use 'high', 'medium', or 'low'.")
                        continue

                tag_input = input("Filter by tag or press Enter to skip: ").strip()
                if tag_input:
                    tags = [tag_input]

                filtered_tasks = todo_list.filter_tasks(status=status, priority=priority, tags=tags)

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
                continue

            if not filtered_tasks:
                print("No tasks match the specified filters. Try different filter criteria.")
            else:
                print(f"\nFound {len(filtered_tasks)} task(s) matching the filters:")
                print("\nID Pri Status Title               Description Tags")
                for task in filtered_tasks:
                    print(format_task_display(task))

        elif choice == "11":
            # Sort tasks
            print("\nSort options:")
            print("1. By priority (High → Low)")
            print("2. By title (Alphabetical)")
            print("3. By status (Completed first)")

            sort_choice = input("Choose sort type (1-3): ").strip()

            if sort_choice == "1":
                sort_by = "priority"
            elif sort_choice == "2":
                sort_by = "title"
            elif sort_choice == "3":
                sort_by = "status"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue

            all_tasks = todo_list.get_all_tasks()
            sorted_tasks = todo_list.get_sorted_tasks(all_tasks, sort_by=sort_by)

            if not sorted_tasks:
                print("No tasks to display.")
            else:
                print(f"\nTasks sorted by {sort_by}:")
                print("\nID Pri Status Title               Description Tags")
                for task in sorted_tasks:
                    print(format_task_display(task))

        elif choice == "12":
            # Exit
            print("Thank you for using the Todo Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 12.")


if __name__ == "__main__":
    main()