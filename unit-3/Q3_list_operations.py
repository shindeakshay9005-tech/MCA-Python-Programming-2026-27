# Unit 3 - Q3: List Operations and List Comprehension

n = int(input("How many integers? "))
numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(n)]
print("Original list:", numbers)

# Insert and remove at specified positions
pos = int(input("Position to insert at: "))
val = int(input("Value to insert: "))
numbers.insert(pos, val)
print("After insert:", numbers)

rem = int(input("Value to remove: "))
if rem in numbers:
    numbers.remove(rem)
print("After remove:", numbers)

# Sorting
ascending = sorted(numbers)
numbers.sort(reverse=True)
print("Ascending  :", ascending)
print("Descending :", numbers)
numbers.reverse()

# Max, min, sum
print("Maximum:", max(numbers), "| Minimum:", min(numbers), "| Sum:", sum(numbers))

# Concatenation, repetition, indexing, membership
print("Concatenation:", numbers + [0])
print("Repetition:", [1, 2] * 3)
print("Indexing (first, last):", numbers[0], numbers[-1])
print("Membership (numbers contains 5):", 5 in numbers)

# List methods
other = [100, 200]
numbers.append(99)
numbers.extend(other)
print("After append() and extend():", numbers)
popped = numbers.pop()
print("pop() returned:", popped, "| list now:", numbers)

# List comprehension
print("Even numbers :", [x for x in numbers if x % 2 == 0])
print("Odd numbers  :", [x for x in numbers if x % 2 != 0])
print("Squares      :", [x ** 2 for x in numbers])
