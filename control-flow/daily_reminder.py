# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case 'high':
        reminder_message = f"'{task}' is a high priority task"
        if time_bound == 'yes':
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += "."
    case 'medium':
        reminder_message = f"'{task}' is a medium priority task"
        if time_bound == 'yes':
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += "."
    case 'low':
        reminder_message = f"'{task}' is a low priority task."
        if time_bound == 'yes':
            reminder_message += " Consider completing it soon."
        else:
            reminder_message += " Consider completing it when you have free time."
    case _:
        reminder_message = "Invalid priority level entered."

# Provide a Customized Reminder
print(reminder_message)
