# Unit 4 - Q4(3): datetime library

from datetime import datetime, date

now = datetime.now()
print("Current date and time:", now.strftime("%d-%m-%Y %H:%M:%S"))

today = date.today()
print("Day:", today.day, "| Month:", today.month, "| Year:", today.year)

d1 = date(2026, 1, 1)
d2 = date.today()
diff = d2 - d1
print(f"Difference between {d1} and {d2}: {diff.days} days")

# Custom dates entered by user
s1 = input("Enter first date (YYYY-MM-DD): ")
s2 = input("Enter second date (YYYY-MM-DD): ")
first = datetime.strptime(s1, "%Y-%m-%d").date()
second = datetime.strptime(s2, "%Y-%m-%d").date()
print("Days between the two dates:", abs((second - first).days))
