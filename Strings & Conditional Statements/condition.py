age = 21
if(age >= 18):
# #     OR
# # if(True):
    print("I Can vote & apply for License")
    print("I can drive")

light = "Green"
if(light == "Red"):
    print("Stop")
elif(light == "Green"):
    print("Go")
elif(light == "Yellow"):
    print("Look")

print("End of Code")


light = "Pink"
if(light == "Red"):
    print("Stop")
elif(light == "Green"):
    print("Go")
elif(light == "Yellow"):
    print("Look")
else:
    print("Light is broken")

age = 17
if(age >= 18):
    print("Can vote")
else:
    print("Can't vote")


marks = int(input("Enter Students Mark's - "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student is -", grade)

age = 95
if(age >= 18):
    if(age >= 80):
        print("Can't drive")
    else:
        print("Can drive")
else:
    print("Can't dirve")