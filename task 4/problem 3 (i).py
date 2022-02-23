lst = []
x = int(input("Enter number of rows : "))
print("Enter the roll number , name and marks respectively to output a data table")
for i in range(0, x):
    ele = [input(), input(),input()]
    lst.append(ele)
print("Enter the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for p in lst:
    for q in p:
        print(q,end=" "*10)
    print()
