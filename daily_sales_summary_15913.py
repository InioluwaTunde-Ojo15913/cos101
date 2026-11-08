step = 1
while step == 1:
    days = int(input("How many days was the shop open: "))
    if days <= 0:
        print("Invalid number of days")
    else:
        step = 2
        
total_sales = 0
good_days = 0
bad_days = 0

while step == 2:
       for day in range(1, days + 1):
           unaccept_day = True
           while unaccept_day:
               sale = float(input(f"Enter sales for day {day}: "))
               if sale <= 0:
                   print("Invalid sales value.")
               else:
                   step = 3
                   if sale >= 10000:
                       good_days = good_days + 1
                   else:
                       bad_days = bad_days + 1
                   unaccept_day = False
           total_sales = total_sales + sale

average_sales = total_sales / days
print(days)
print(f"Total sales: NGN{total_sales:,.2f}")
print(f"Average daily sales: {average_sales:,.2f}")
print(f"Days with sales of at least NGN 10,000: {good_days}")
print(f"Days with sales below NGN 10,000: {bad_days}")
