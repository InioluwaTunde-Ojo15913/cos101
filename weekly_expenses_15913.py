name = input("Enter your name: ")
transport_cost = float(input("Enter daily transport cost (NGN): "))
feeding_cost = float(input("Enter daily feeding cost (NGN): "))
days_on_campus = float(input("Enter number of days on campus: "))
other_expenses = float(input("Enter other expenses for the week: "))
transport_total = transport_cost * days_on_campus
feeding_total = feeding_cost * days_on_campus
weekly_total = transport_total + feeding_cost + other_expenses
print("===================================================")
print("WEEKLY EXPENSE SUMMARY")
print("Student: ", name)
print("Transport total: NGN ", transport_total)
print("Feeding total: NGN ", feeding_total)
print("Other expenses: NGN ", other_expenses)
print("Weekly total: NGN ", weekly_total)

