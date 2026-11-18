# Unit 3 - Q5: Dictionaries, Dictionary Comprehension and Nested Collections

employees = {
    101: {"name": "Asha", "department": "IT", "salary": 55000},
    102: {"name": "Rahul", "department": "HR", "salary": 42000},
    103: {"name": "Meera", "department": "Finance", "salary": 61000},
}

# Add
employees[104] = {"name": "Kiran", "department": "IT", "salary": 58000}

# Update
employees[102]["salary"] = 45000

# Delete
del employees[103]

# Keys, values and key-value pairs
print("Keys:", employees.keys())
print("Values:")
for value in employees.values():
    print("  ", value)
print("Key-value pairs:")
for key, value in employees.items():
    print(f"  {key}: {value}")

# Search by employee ID
emp_id = int(input("\nEnter employee ID to search: "))
if emp_id in employees:
    print("Employee found:", employees[emp_id])
else:
    print("Employee not found")

# Dictionary comprehension: employees earning above a salary
threshold = int(input("Enter salary threshold: "))
above = {eid: info for eid, info in employees.items() if info["salary"] > threshold}
print(f"Employees earning above {threshold}:", above)
