while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if priority in ["high", "medium", "low"] and time_bound in ["yes", "no"]:
        break
    else:
        print("Invalid input. Please try again.\n")

match priority:
    case "high":
            message = f"{task} is a high priority task."
    case "medium":
            message = f"{task} is a medium priority task."
    case "low":
            message = f"{task} is a low priority task"

if time_bound == "yes":
    message += " that requires immediate attention today."
else:
    message += " that can be addressed later. Consider completing it when you have free time."

print("Reminder:", message)
             