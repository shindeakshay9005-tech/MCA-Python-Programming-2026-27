basic = float(input("Enter Basic Salary: "))

da = basic * 10 / 100
hra = basic * 20 / 100

gross = basic + da + hra

tax = gross * 5 / 100

net = gross - tax

print("DA =", da)
print("HRA =", hra)
print("Gross Salary =", gross)
print("Tax =", tax)
print("Net Salary =", net)