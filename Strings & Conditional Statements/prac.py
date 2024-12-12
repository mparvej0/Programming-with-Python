name = input("Enter Your Name - ")
print("Length of Your name is", len(name))

str = "Hi, $Iam the $ symbol $99.99"
print(str.count("$"))

num = int(input("Enter Number : "))
rem = num % 2
if(rem == 0):
    # OR
# if(num % 2 == 0):
    print("Even")
else:
    print("odd")

a = int(input("Enter First Number : "))
b = int(input("Enter First Number : "))
c = int(input("Enter First Number : "))
if(a >= b and a >= c):
    print("First number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("second number is largest", c)

x = int(input("Enter number: "))
if(x % 7 == 0):
    print("Multiple of 7")
else:
    print("Not a Multiple")


