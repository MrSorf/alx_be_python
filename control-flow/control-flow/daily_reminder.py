task = str(input("Enter a task description"))

priority = str(input("Choose priority(high, medium, low)"))

time_bound = str(input("Is the task time-bound(yes or no)"))

match priority:
    case "high":
        reminder = f"Task: {task} high priority"
    case "low":
        reminder = f"Task: {task} low priority"
    case "medium":
        reminder = f"Task: {task} medium priority"
    case _:
        reminder = f"Task: {task} unknown priority"

if time_bound == "yes":
    print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note: {task} is a low priority task. Consider completing it when you have free time")
else:
    print("please include a valid task!")