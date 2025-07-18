task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): "))
time_bound = str(input("Is it time-bound? (yes/no):"))

priority = priority.lower()
time_bound = time_bound.lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder:'{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task. that requires immediate attention today!")
        else:
            print(f"Reminder:'{task}' is medium priority. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task. that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")