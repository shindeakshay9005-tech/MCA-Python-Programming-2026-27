# Unit 4 - Q3: File Methods and File-Related Exception Handling
# Expects student.txt (created by Q2). Run Q2 first if it is missing.

FILENAME = "student.txt"

try:
    f = open(FILENAME, "r")
except FileNotFoundError:
    print(f"Error: {FILENAME} does not exist")
except PermissionError:
    print(f"Error: no permission to open {FILENAME}")
else:
    print("File name:", f.name)
    print("File mode:", f.mode)

    # read()
    content = f.read()
    print("\nread() returned", len(content), "characters")

    # seek() and tell()
    print("Position after read():", f.tell())
    f.seek(0)
    print("Position after seek(0):", f.tell())

    # readline()
    f.seek(0)
    print("\nreadline() ->", f.readline().rstrip())
    print("Position now:", f.tell())

    # readlines()
    f.seek(0)
    print("\nreadlines():")
    for line in f.readlines():
        print(" ", line.rstrip())
    f.close()
finally:
    print("\nFile operation finished")
