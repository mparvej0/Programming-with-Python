#function definition
def calc_sum(a, b): #parameters
    sum = a + b
    print(sum)
    return(sum)
calc_sum(5, 10) #15, function call; arguments
#OR
def calc_sum(a, b): #parameters
    return a + b
sum = calc_sum(1, 2) #3, function call; arguments
print(sum)

def print_hello():
    print("Hello")
print_hello()
print_hello()

output = print_hello()
print(output)

#average of 3 numbers
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
calc_avg(98, 97, 95)

#Built-in Functiions
print("Soas University", end=" ") #seperate line
print("of London") #end

#Default Parameters
def calc_prod(a=4, b=2):
    print(a * b)
    return a * b
calc_prod()