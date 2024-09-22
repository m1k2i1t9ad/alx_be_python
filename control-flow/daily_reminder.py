# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize the reminder message
reminder = f"'{task}' is a {priority} priority task."

# Process the Task Based on Priority Using Match Case
match priority:
    case 'high':
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Note: {reminder}. Consider completing it when you have free time.")
    case 'medium':
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Note: {reminder}. Consider completing it when you have free time.")
    case 'low':
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Note: {reminder}. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered.")
