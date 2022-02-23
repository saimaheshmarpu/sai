a =int (input("Enter a number:"))
p = a
rev=0
while(a > 0):
    dig = a % 10
    rev = rev*10+dig
    a = a//10
if(p==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
