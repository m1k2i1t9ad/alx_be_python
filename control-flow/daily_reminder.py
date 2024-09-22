# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize the reminder message
reminder = f"'{task}' is a {priority} priority task"

# Provide Customized Output Based on Priority and Time Sensitivity
if time_bound == "yes" or priority == "high":
    print(f"Reminder: {reminder} that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note: {reminder}. Consider completing it when you have free time.")
else:
    print("Invalid input for time sensitivity.")
