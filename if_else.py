a = int(input("Enter your age"))
print("Your age is:",a)
# # conditional operators >, <, >=, <=, ==, !=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
if(a>18):
    print("You can drive")
    print("Yes")
else:
    print("You can't drive")
    print("NO")

# Short hand if else statements.
a = 330
b = 3303
print("A") if a>b else print("a") if a == b else print("B")

c = 9 if a>b else 0
print(c)
