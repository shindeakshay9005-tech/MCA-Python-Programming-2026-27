# Unit 4 - Q2: File Handling - Read, Write and Append
# Works on student.txt in the same folder as this script.

FILENAME = "student.txt"

# Create and open in write mode, then accept and write details
f = open(FILENAME, "w")
n = int(input("How many students to add? "))
for i in range(n):
    name = input(f"Name of student {i + 1}: ")
    roll = input("Roll number: ")
    cls = input("Class: ")
    f.write(f"{roll},{name},{cls}\n")
f.close()

# Read and display the complete file
print("\n--- Complete file contents ---")
with open(FILENAME, "r") as f:
    print(f.read())

# Append more records without deleting existing ones
f = open(FILENAME, "a")
more = int(input("How many more students to append? "))
for i in range(more):
    name = input(f"Name of new student {i + 1}: ")
    roll = input("Roll number: ")
    cls = input("Class: ")
    f.write(f"{roll},{name},{cls}\n")
f.close()

# Read line by line
print("\n--- Reading line by line ---")
f = open(FILENAME, "r")
for line in f:
    print(line.strip())
f.close()

# Display all lines using readlines()
f = open(FILENAME, "r")
lines = f.readlines()
f.close()
print("\n--- All lines (readlines) ---")
for line in lines:
    print(line.rstrip())
