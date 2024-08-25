name = "Raju"
friend = "Devil"
anotherFriend = "Frick"
apple = '''He said,
Hi Harry
hey I am good
"I want to eat an apple'''

print("Hello, " + name) # type: ignore
#print(apple)
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
print(fruit[1:4])
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

str1 = "Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalnum())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christian/n"
print(str1.isprintable())
str1 = " " # Using Spacebar
print(str1.isspace())
str2 = " " # Using Tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())