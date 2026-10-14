list=[]

for i in range(3):
    row = []
    for j in range(3):
        val = int(input("Enter your Number: "))
        row.append(val)
    list.append(row)
print(list)

for i in range(3):
    for j in range (3):
        print(list[i][j],end=" ")
    print()
    
        