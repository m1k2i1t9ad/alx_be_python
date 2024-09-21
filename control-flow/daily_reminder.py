# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize the reminder message
reminder_message = ""

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case 'high':
        reminder_message = f"'{task}' is a high priority task."
    case 'medium':
        reminder_message = f"'{task}' is a medium priority task."
    case 'low':
        reminder_message = f"'{task}' is a low priority task."
    case _:
        reminder_message = "Invalid priority level entered."
        print(reminder_message)
        exit()

# Determine if the task is time-bound and modify the reminder
if time_bound == 'yes':
    reminder_message += " It requires immediate attention today!"
else:
    reminder_message += " Consider completing it when you have free time."

# Provide a Customized Reminder
print(reminder_message)
