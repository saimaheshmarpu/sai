lst = []
a = int(input("Enter number of elements : "))
print("Enter the roll number , name and marks respectively to output a data table")
for i in range(0, a):
    ele = [input(), input(),input()]
    lst.append(ele)
print("Enter the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for i in range(3):
    print(lst[1][i], end=" "*10)