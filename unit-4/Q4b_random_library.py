# Unit 4 - Q4(2): random library

import random

print("Random integer (1-100):", random.randint(1, 100))

fruits = ["apple", "banana", "mango", "grape", "orange"]
print("Random element:", random.choice(fruits))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)
