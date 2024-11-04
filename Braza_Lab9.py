Num = int(input("Enter the number of rows: "))

i = 1
for y in range(1, Num + 1):
    for x in range(1, y + 1):
        print(i,end=" ")
        i = i+1
    print()
