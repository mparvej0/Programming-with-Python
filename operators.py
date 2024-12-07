#Arithmetic Operatos
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #Remainder eg. 5/2 = 1 is remainder
print(a ** b) #a^b a raised to the power of b

#Relational Operators
a = 50
b = 20

print(a == b) #False ==( equal to)
print(a != b) #True !=(not equalt to)
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b) #False

#Assignment Operators
num = 10
# num = num + 10 #10+10 =>20
num += 10
print("num : ", num)

num = 10
num *= 5
print("num :", num) #Ansers is 20

num = 10
num /= 5
print("num :", num)

#Logical Operator
a = 50
b = 30
print(not False)
print(not (a > b))

val1 = False
val2 = False
print("AND operator:", val1 and val2)
print("OR operator:", (a == b) or (a > b))
