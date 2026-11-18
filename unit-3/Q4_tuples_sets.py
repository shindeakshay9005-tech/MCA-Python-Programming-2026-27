# Unit 3 - Q4: Tuples, Sets and Set Operations

# Tuple of roll numbers
roll_tuple = (101, 102, 103, 104, 105)
print("Tuple of roll numbers:", roll_tuple)

# Indexing, slicing, concatenation
print("Indexing (first, last):", roll_tuple[0], roll_tuple[-1])
print("Slicing [1:4]:", roll_tuple[1:4])
print("Concatenation:", roll_tuple + (106, 107))

# Two sets of roll numbers from different courses
course_a = {101, 102, 103, 104}
course_b = {103, 104, 105, 106}
print("\nCourse A:", course_a)
print("Course B:", course_b)

print("Union:", course_a | course_b)
print("Intersection:", course_a & course_b)
print("Difference (A - B):", course_a - course_b)
print("Symmetric difference:", course_a ^ course_b)

# Subset and superset
subset_check = {103, 104}
print("\nIs {103, 104} subset of Course A?", subset_check.issubset(course_a))
print("Is Course A superset of {103, 104}?", course_a.issuperset(subset_check))

# Add and remove elements
course_a.add(110)
print("After add(110):", course_a)
course_a.remove(110)
print("After remove(110):", course_a)

# Set comprehension: squares of even numbers in a range
start = int(input("\nRange start: "))
end = int(input("Range end: "))
even_squares = {x ** 2 for x in range(start, end + 1) if x % 2 == 0}
print("Set of squares of even numbers:", even_squares)
