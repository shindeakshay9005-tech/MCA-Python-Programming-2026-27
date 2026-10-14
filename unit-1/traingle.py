list = [[1,2,3],[4,5,6],[7,8,9]]

for i in range (3) :
    for j in range (3):
        print(list[i][j], end = " ")
    print()
    
    
print("Diagonal  matrix")
for i in range (3):
    for j in range (3):
        if i == j :
            print(list[i][j], end=" ")
        else :
            print("0",end=" ")
    print()
    
    
print("Lower Traigular")
for i  in range (3):
    for j in range (3):
        if i >= j:
            print(list[i][j],end=" ")
        else:
            print("0",end=" ")
    print()
    
    
print("Upper Traingular")
for i in range (3):
    for j in range (3):
        if i<=j:
            print(list[i][j],end=" ")
        else:
            print("0",end = " ")
    print()    