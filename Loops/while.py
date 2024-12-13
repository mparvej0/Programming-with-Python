# while True :
#     print("Raju") #enfinite print

count = 1
while count <= 5:
    print("Hello") #five times print
    count += 1
print(count)

i = 1
while i <= 5:
    print("World", i)
    i+=1

#print numbers form 1 o 5
i = 1
while i <= 5:
    print(i)
    i += 1

i = 5
while i >= 1:
    print(i)
    i -=1
print("Loop Ended")


#Break
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("Loop Ended")

#Continue
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue #skip
    print(i)
    i += 1
print("Loop Ended")
n = 1
while n <= 10:
    if(n%2 == 0): #for odd number
    # if(n&2 != 0): #for even number
        n += 1
        continue #skip
    print(n)
    n += 1