# Unit 3 - Q1: String Operations and String Methods

sentence = input("Enter a sentence: ")

print("Length of string:", len(sentence))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("After strip():", f"[{sentence.strip()}]")

old_word = input("Word to replace: ")
new_word = input("Replace with: ")
print("After replace:", sentence.replace(old_word, new_word))

char = input("Character to count: ")
print(f"Occurrences of '{char}':", sentence.count(char))

prefix = input("Check if string starts with: ")
suffix = input("Check if string ends with: ")
print("Starts with prefix:", sentence.startswith(prefix))
print("Ends with suffix:", sentence.endswith(suffix))

# Concatenation, repetition and membership
first, second = "Hello", "World"
print("Concatenation:", first + " " + second)
print("Repetition:", first * 3)
print("Membership ('ell' in 'Hello'):", "ell" in first)
print("Not-membership ('xyz' not in 'Hello'):", "xyz" not in first)
