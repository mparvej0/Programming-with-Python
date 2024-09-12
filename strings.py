name = "Raju"
apple = '''He said,
Hi Harry
hey I am good
"I want to eat an apple'''
print("Hello, " + name) 
print(apple)
print(name[0])
print(name[1])
print(name[2])

print("Lets use a for loop\n")
for character in apple:
    print(character)

# string Silicing and Operations
fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4])
print(fruit[:5])
print(fruit[:len(fruit)-3]) # Python automatically use len of fruit
print(fruit[-1:-3])
print(fruit[-3:-1])

nm = "Harry"
print(nm[-4:-2])

# String Methods
# Strings are immutable
a = "!!!Harry!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str0 = "Welcome to the console!!!"
print(len(str0))
print(len(str0.center(50)))
print(a.count("Harry"))
print(str0.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str2 = "He's name is Dan. He is an honest man."
print(str2.find("is"))

str3 = "Welcome"
print(str3.isalnum())

str4 = "hello world"
print(str4.islower())

str5 = "We wish you a Merry Christian/n"
print(str5.isprintable())

str6 = " " # Using Spacebar
print(str6.isspace())

str7 = "World Health Organization"
print(str7.istitle())

str8 = "Python is a Interpreted Language"
print(str8.startswith("Python"))

str9 = "Python is a Interpreted Language"
print(str9.swapcase())

str10 = "His name is Dan. Dan is an honest man."
print(str10.title())