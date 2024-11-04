Num = int(input("Enter the number of rows: "))

i = 1
for y in range(1, Num + 1): 
    for x in range(1, y + 1): # for row == Num
        print(i,end=" ") # avoid single line per row 
        i = i+1
    print()
