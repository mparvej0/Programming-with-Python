# Conditional operators >, <, >=, <=, ==, !=
# If & Else Condition
a = int(input("Enter your age"))
print("Your age is:", a )
if(a>18):
    print("You can drive")
    print("Yes")
else:
    print("You can't drive")
    print("NO")

# If, elif & else

num = int(input("Enter the value of num:"))
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")