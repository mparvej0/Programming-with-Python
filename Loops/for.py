nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val)

veggies = ["Potato", "Brinjal", "Ladyfinger","Cucumber"]
for val in veggies:
    print(val)

tup = (1, 2, 3, 4, 2, 8, 9)
for num in tup:
    print(num)

str = "Soas University of London"
for char in str:
    if(char == "U"):
        print("U Found")
        break
    print(char)
else:
    print("END")

#Rang()
for i in range(10): #range(stop)
    print(i)
for i in range(2, 10): #range(start, stop)
    print(i)
for i in range(2, 10, 2): #range(start, stop, step)
    print(i)

#Pass Statement
for i in range(5):
    pass
#OR
if i > 5:
    pass
print("Some useful work")