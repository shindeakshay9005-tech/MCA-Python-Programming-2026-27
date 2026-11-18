# Unit 3 - Q2: String Slicing and String Formatting

full_name = input("Enter full name (First Last): ").strip()
email = input("Enter email address: ").strip()
mobile = input("Enter mobile number: ").strip()

# Split first and last name using slicing
space_index = full_name.find(" ")
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]

# Reverse the name using slicing
reversed_name = full_name[::-1]

# Username and domain from email
at_index = email.find("@")
username = email[:at_index]
domain = email[at_index + 1:]

# Last four digits of mobile number
last_four = mobile[-4:]

# Positive and negative indexing
print("Positive index  full_name[0]:", full_name[0])
print("Negative index  full_name[-1]:", full_name[-1])

# Display using f-string and other formatting techniques
print(f"\nFirst name : {first_name}")
print(f"Last name  : {last_name}")
print("Reversed   : {}".format(reversed_name))
print("Username   : %s" % username)
print(f"Domain     : {domain}")
print(f"Mobile (last 4 digits): {last_four}")
print(f"{'STUDENT INFORMATION':^40}")
print(f"{'-' * 40}")
print(f"{'Full Name':<15}{full_name:>25}")
print(f"{'Email':<15}{email:>25}")
