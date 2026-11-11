name = input("Enter your name: ")
transport_cost = int(input("Enter daily transport cost (NGN): "))
feeding_cost = int(input("Enter daily feeding cost (NGN): "))
days_on_campus = int(input("Enter number of days on campus: "))
other_expenses = int(input(f"Enter other expenses for {days_on_campus} days: "))
budget = int(input(f"Enter your budget for {days_on_campus} days: "))
if transport_cost < 0 or feeding_cost < 0 or days_on_campus < 0 or other_expenses < 0:
    print("Invalid input entered")
else:
    transport_total = transport_cost * days_on_campus
    feeding_total = feeding_cost * days_on_campus
    total = transport_total + feeding_total + other_expenses
    print("===================================================")
    print("WEEKLY EXPENSE SUMMARY")
    print("Student: ", name)
    print("Transport total: NGN ", transport_total)
    print("Feeding total: NGN ", feeding_total)
    print("Other expenses: NGN ", other_expenses)
    print(f"Total for {days_on_campus} days: NGN ", total)
    if total < budget:
        print("Within budget")
        print(f"{budget - total} is remaining.")
    elif total == budget:
        print("Exactly on budget")
    else:
        print("Over budget")
        print(f"You are {total - budget} over budget.")
