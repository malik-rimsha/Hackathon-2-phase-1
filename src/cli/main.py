"""
Todo application CLI interface.
"""
import argparse
from datetime import datetime
from typing import Optional

from ..services.task_service import TaskService
from ..models.task import Task, Priority
from ..models.recurrence import RecurrenceInterval


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
    print("12. Set due date for task")
    print("13. Set recurrence for task")
    print("14. Exit")


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
    Format a task for display with due dates and recurrence indicators.

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

    # Format due date
    due_date_str = ""
    if task.due_datetime:
        if task.due_datetime < datetime.now():
            due_date_str = f" (Overdue: {task.due_datetime.strftime('%Y-%m-%d %H:%M')})"
        elif task.due_datetime.date() == datetime.now().date():
            due_date_str = f" (Due Today: {task.due_datetime.strftime('%H:%M')})"
        else:
            due_date_str = f" (Due: {task.due_datetime.strftime('%Y-%m-%d %H:%M')})"

    # Format recurrence
    recurrence_str = ""
    if task.recurrence:
        recurrence_map = {
            RecurrenceInterval.DAILY: "🔁 Daily",
            RecurrenceInterval.WEEKLY: "🔁 Weekly", 
            RecurrenceInterval.MONTHLY: "🔁 Monthly"
        }
        recurrence_str = f" {recurrence_map.get(task.recurrence, '')}"

    # Format tags
    tags_display = ""
    if task.tags:
        tags_display = " " + " ".join([f"#{tag}" for tag in task.tags])

    return f"{task.id:2d} {priority_indicator} {status} {task.title:<20} {task.description}{due_date_str}{recurrence_str}{tags_display}"


def main():
    """
    Main application loop with menu-driven interface.
    """
    task_service = TaskService()

    while True:
        display_menu()
        choice = input("Enter your choice (1-14): ").strip()

        if choice == "1":
            # Add a new task
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            
            # Ask for recurrence
            recurrence_input = input("Enter recurrence (daily/weekly/monthly) or press Enter to skip: ").strip().lower()
            recurrence = None
            if recurrence_input:
                if recurrence_input in ['daily', 'd']:
                    recurrence = RecurrenceInterval.DAILY
                elif recurrence_input in ['weekly', 'w']:
                    recurrence = RecurrenceInterval.WEEKLY
                elif recurrence_input in ['monthly', 'm']:
                    recurrence = RecurrenceInterval.MONTHLY
                else:
                    print("Invalid recurrence. Use 'daily', 'weekly', or 'monthly'.")
                    continue

            # Ask for due date
            due_date_input = input("Enter due date (YYYY-MM-DD) or relative term (today/tomorrow) or press Enter to skip: ").strip()
            due_datetime = None
            if due_date_input:
                time_input = input("Enter due time (HH:MM) or press Enter for start of day: ").strip()
                # We'll need to parse this date in the service
                # For now, we'll just pass the string to the service to handle
                from datetime import datetime, timedelta
                if due_date_input.lower() == "today":
                    base_date = datetime.now().date()
                elif due_date_input.lower() == "tomorrow":
                    base_date = (datetime.now() + timedelta(days=1)).date()
                else:
                    try:
                        base_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Use YYYY-MM-DD.")
                        continue
                
                if time_input:
                    try:
                        time_obj = datetime.strptime(time_input, "%H:%M").time()
                        due_datetime = datetime.combine(base_date, time_obj)
                    except ValueError:
                        print("Invalid time format. Use HH:MM.")
                        continue
                else:
                    due_datetime = datetime.combine(base_date, datetime.min.time())

            task_id = task_service.add_task(title, description, recurrence, due_datetime)
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
                print("4. By due date (overdue/due-today/due-soon)")
                print("5. By recurrence")
                print("6. Combined filters")

                filter_choice = input("Choose filter type (1-6): ").strip()

                if filter_choice == "1":
                    status_input = input("Filter by status (completed/pending): ").strip().lower()
                    # For this implementation, we'll just show all tasks with the filter applied in the display
                    tasks = task_service.get_all_tasks()
                    if status_input in ['completed', 'done', 'finished']:
                        tasks = [t for t in tasks if t.completed]
                    elif status_input in ['pending', 'incomplete', 'todo']:
                        tasks = [t for t in tasks if not t.completed]
                    else:
                        print("Invalid status. Please use 'completed' or 'pending'.")
                        continue

                elif filter_choice == "2":
                    priority_input = input("Filter by priority (high/medium/low): ").strip().lower()
                    tasks = task_service.get_all_tasks()
                    if priority_input == "high":
                        tasks = [t for t in tasks if t.priority == Priority.HIGH]
                    elif priority_input == "medium":
                        tasks = [t for t in tasks if t.priority == Priority.MEDIUM]
                    elif priority_input == "low":
                        tasks = [t for t in tasks if t.priority == Priority.LOW]
                    else:
                        print("Invalid priority. Please use 'high', 'medium', or 'low'.")
                        continue

                elif filter_choice == "3":
                    tag_input = input("Filter by tag: ").strip()
                    if not tag_input:
                        print("No tag provided. Please enter a valid tag.")
                        continue
                    tasks = task_service.get_all_tasks()
                    tasks = [t for t in tasks if tag_input in t.tags]

                elif filter_choice == "4":
                    due_filter = input("Filter by due date (overdue/due-today/due-soon): ").strip().lower()
                    if due_filter in ["overdue", "due-today", "due-soon"]:
                        tasks = task_service.get_tasks_with_filter(due_filter)
                    else:
                        print("Invalid due date filter. Use 'overdue', 'due-today', or 'due-soon'.")
                        continue

                elif filter_choice == "5":
                    tasks = task_service.get_tasks_with_filter("recurring")

                elif filter_choice == "6":
                    # Combined filters would be more complex to implement in this simple CLI
                    print("Combined filters not implemented in this simple CLI. Please use single filters.")
                    continue

                else:
                    print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
                    continue
            else:
                # No filters - show all tasks
                tasks = task_service.get_all_tasks()

            # Ask if user wants to sort the results
            sort_choice = input("Apply sorting? (y/n): ").strip().lower()
            if sort_choice in ['y', 'yes']:
                print("\nSort options:")
                print("1. By priority (High → Low)")
                print("2. By title (Alphabetical)")
                print("3. By due date (Earliest first)")
                print("4. By status (Completed first)")

                sort_choice = input("Choose sort type (1-4): ").strip()

                if sort_choice == "1":
                    tasks = sorted(tasks, key=lambda t: (
                        1 if t.priority == Priority.HIGH else 
                        2 if t.priority == Priority.MEDIUM else 
                        3 if t.priority == Priority.LOW else 999,
                        t.id
                    ))
                elif sort_choice == "2":
                    tasks = sorted(tasks, key=lambda t: t.title.lower())
                elif sort_choice == "3":
                    tasks = sorted(tasks, key=lambda t: t.due_datetime if t.due_datetime else datetime.max)
                elif sort_choice == "4":
                    tasks = sorted(tasks, key=lambda t: (t.completed, t.id))
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")
                    continue

            # Display the tasks
            if not tasks:
                print("\nNo tasks match the specified filters.")
            else:
                print(f"\nShowing {len(tasks)} task(s):")
                print("\nID Pri Status Title               Description")
                for task in tasks:
                    print(format_task_display(task))

        elif choice == "3":
            # Update a task
            try:
                task_id = int(input("Enter task ID to update: "))
                task = task_service.get_task_by_id(task_id)
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

                success = task_service.update_task(task_id, new_title, new_description)
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
                success = task_service.delete_task(task_id)
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
                task = task_service.get_task_by_id(task_id)
                if task is None:
                    print(f"Task with ID {task_id} not found. Please check the ID and try again.")
                    continue

                current_status = "complete" if task.completed else "incomplete"
                new_status = input(f"Mark as complete? (current: {current_status}) [y/n]: ").strip().lower()

                if new_status in ['y', 'yes', '1', 'true']:
                    # Mark as complete, which will handle recurrence if applicable
                    success = task_service.mark_complete(task_id)
                    if success:
                        print(f"Task {task_id} marked as complete.")
                        # If the task was recurring, a new instance should have been created
                        if task.recurrence:
                            print(f"New instance of recurring task created.")
                    else:
                        print(f"Failed to mark task {task_id}.")
                elif new_status in ['n', 'no', '0', 'false']:
                    # Mark as incomplete
                    task.completed = False
                    task.updated_at = datetime.now()
                    update_success = task_service.update_task(task_id, task.title, task.description, 
                                                             task.priority, task.tags, 
                                                             task.due_datetime, task.recurrence)
                    if update_success:
                        print(f"Task {task_id} marked as incomplete.")
                    else:
                        print(f"Failed to update task {task_id}.")
                else:
                    print("Invalid input. Please enter 'y' for complete or 'n' for incomplete.")
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "6":
            # Assign priority to task
            try:
                task_id = int(input("Enter task ID to assign priority: "))
                task = task_service.get_task_by_id(task_id)
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

                success = task_service.update_task(task_id, priority=priority)
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
                task = task_service.get_task_by_id(task_id)
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

                # Get current tags and add new ones
                current_tags = task.tags if task.tags else []
                for tag in tags:
                    if tag not in current_tags:
                        current_tags.append(tag)
                
                success = task_service.update_task(task_id, tags=current_tags)
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
                task = task_service.get_task_by_id(task_id)
                if task is None:
                    print(f"Task with ID {task_id} not found. Please check the ID and try again.")
                    continue

                tags_input = input("Enter tags to remove (comma-separated): ").strip()
                if not tags_input:
                    print("No tags provided. Please enter at least one tag to remove.")
                    continue

                tags_to_remove = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
                if not tags_to_remove:
                    print("No valid tags provided. Please enter at least one valid tag to remove.")
                    continue

                # Get current tags and remove specified ones
                current_tags = task.tags if task.tags else []
                for tag in tags_to_remove:
                    if tag in current_tags:
                        current_tags.remove(tag)
                
                success = task_service.update_task(task_id, tags=current_tags)
                if success:
                    print(f"Tags {', '.join(tags_to_remove)} removed from task {task_id} successfully.")
                else:
                    print(f"Failed to remove tags from task {task_id}.")
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "9":
            # Search tasks - simplified implementation
            keyword = input("Enter keyword to search: ").strip()
            if not keyword:
                print("No keyword provided. Please enter a keyword to search for.")
                continue

            all_tasks = task_service.get_all_tasks()
            matching_tasks = [t for t in all_tasks 
                             if keyword.lower() in t.title.lower() or 
                                keyword.lower() in t.description.lower() or
                                any(keyword.lower() in tag.lower() for tag in t.tags)]
            
            if not matching_tasks:
                print(f"No tasks found containing '{keyword}'. Try a different search term.")
            else:
                print(f"\nFound {len(matching_tasks)} task(s) containing '{keyword}':")
                print("\nID Pri Status Title               Description")
                for task in matching_tasks:
                    print(format_task_display(task))

        elif choice == "10":
            # Filter tasks - already handled in option 2
            print("Filtering is handled in option 2 (View all tasks). Please select that option.")

        elif choice == "11":
            # Sort tasks - already handled in option 2
            print("Sorting is handled in option 2 (View all tasks). Please select that option.")

        elif choice == "12":
            # Set due date for task
            try:
                task_id = int(input("Enter task ID to set due date: "))
                task = task_service.get_task_by_id(task_id)
                if task is None:
                    print(f"Task with ID {task_id} not found. Please check the ID and try again.")
                    continue

                date_input = input("Enter due date (YYYY-MM-DD) or relative term (today/tomorrow): ").strip()
                if not date_input:
                    print("No date provided. Please enter a valid date.")
                    continue

                time_input = input("Enter due time (HH:MM) or press Enter for start of day: ").strip()
                
                success = task_service.set_due_date(task_id, date_input, time_input if time_input else None)
                if success:
                    print(f"Due date set for task {task_id} successfully.")
                else:
                    print(f"Failed to set due date for task {task_id}.")
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "13":
            # Set recurrence for task
            try:
                task_id = int(input("Enter task ID to set recurrence: "))
                task = task_service.get_task_by_id(task_id)
                if task is None:
                    print(f"Task with ID {task_id} not found. Please check the ID and try again.")
                    continue

                recurrence_input = input("Enter recurrence (daily/weekly/monthly): ").strip().lower()
                if not recurrence_input:
                    print("No recurrence provided. Please enter 'daily', 'weekly', or 'monthly'.")
                    continue

                if recurrence_input in ['daily', 'd']:
                    recurrence = RecurrenceInterval.DAILY
                elif recurrence_input in ['weekly', 'w']:
                    recurrence = RecurrenceInterval.WEEKLY
                elif recurrence_input in ['monthly', 'm']:
                    recurrence = RecurrenceInterval.MONTHLY
                else:
                    print("Invalid recurrence. Use 'daily', 'weekly', or 'monthly'.")
                    continue

                success = task_service.set_recurrence(task_id, recurrence)
                if success:
                    print(f"Recurrence '{recurrence_input}' set for task {task_id} successfully.")
                else:
                    print(f"Failed to set recurrence for task {task_id}.")
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")

        elif choice == "14":
            # Exit
            print("Thank you for using the Todo Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 14.")


if __name__ == "__main__":
    main()