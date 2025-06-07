Task = input("Enter a task description: ")

Priority = input("Enter task priority(high, medium, low): ")

time_bound = input("Is the task time-bound(yes or no): ")

match Priority: 
    case "high":
        reminder = f"'{Task}' is a high priority task"
    case "medium":
        reminder = f"'{Task}' is a medium priority task"
    case "low":
        reminder = f"'{Task}' is a low priority task"
    case _:
        reminder = f"'{Task}' has an unknown priority level"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the reminder
print("Reminder:", reminder)
