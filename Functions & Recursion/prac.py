cities = ["Ddlhi", "Gurgaon", "Noida", "Pune", "Mumbai", "Chennai"]
heroes = ["Thor", "Ironman", "Captain America," "Shaktiman"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes)

def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(heroes)
print_list(cities)
print()

n = 5
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)
cal_fact(5)

#Convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")
converter(57)

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(5)
print(sum)

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
fruits = ["Mango", "Lichi", "Apple", "Banana"]
print_list(fruits)