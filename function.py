import numbers


def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesster(a, b):
    pass

a = 9
b = 8
isGreater(a, b)
calculateGmean(a,b)

# if(a>b):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")

# gmean = (a*b)/(a+b)
# print(gmean)

c = 8
d = 7
isGreater(c, d)
calculateGmean(c,d)

# if(c>d):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")

# gmean1 = (c*d)/(c+d)
# print(gmean1)

# def average(a=9,b=1):
#     print("The average is", (a+b)/2)


def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is:", sum/len(numbers))
    # return 7
    return sum / len(numbers)
c = average(5, 6, 7, 1)
print(c)

# average(4, 6)
   # OR
# average(b=9)
     # OR
# average(b=9, a=21)


def name(fname, mname= "Jhon", lname = "Whatson"):
    print("Hello, ", fname, mname, lname)
name("Amy", "Agarwal", "Jain")

# Enumerate Function
marks = [12, 56, 32, 98, 12, 45, 1, 4]

index = 0
for mark in marks:
    print(mark)
    if(index == 3):
      print("Raju, awesome!")
index +=1

for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("Raju, awesome!")