#While Loops
i = 1
while i <= 100:
    print(i)
    i += 1

j = 100
while j >= 1: #stopping condition
    print(j)
    j -= 1

l = 1
while l <= 10:
    print(3*l)
    l += 1
#OR
n = int(input("Enter Number :"))
n1 = 1
while n1 <= 10:
    print(n*n1)
    n1 += 1

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(len(nums))
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
#OR
idx = 0
while idx < len(nums):
    print(nums[idx]) #nums[0], nums[1], nums[2]...
    idx += 1
#OR
heroes = ["Ironman", "Thor", "Superman", "Batman"]
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36
n2 = 0
while n2 < len(num):
    if(num[n2] == x):
        print("FOUND at idx", n2)
        break
    else:
        print("Finding...")
    n2 += 1
print("End of loop")

#For Loops
num1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in num1:
    print(el)

num2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
y = 49
idy = 0
for el in num2:
    if(el == y):
        print("Number found at idx", idy)
        idy += 1

for i in range(1, 100):
    print(i)

for i in range(100, 0, -1):
    print(i)

n3 = int(input("Enter Number :"))
for i in range(1, 11):
    print(n3 * i)

n4 = 5
sum = 0
for i in range(1,n4+1):
    sum += i
print("Total Sum =", sum)
#OR
n5 = 7
sum1 = 0
i = 1
while i <= n5:
    sum1 += i
    i += 1
print("Total Sum =", sum1)


n6 = 9
fact = 1
i = 1
while i <= n6:
    fact *= i
    i += 1
print("Factorial =", fact)
#OR
n7 = 11
fact1 = 1
for  i in range(1, n7+1):
    fact1 *= i
    print("Factorial", fact1)