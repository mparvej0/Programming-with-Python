tup = (1, 2, 76, 342, 32, "green", True)
tup[:]
tup[0:]
tup[0:3]
# tup = (90,)

print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[-1])
print(tup[2])

if 342 in tup:
    print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)

# Change in Tuple
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia") # Add Item
temp.pop(3) # Remove Item
temp[2] = "Finland" # Change Item
countries = tuple(temp)
print(countries)

# Merge Tuple
countries = ("Pakistan", "Afganistan", "Bangladesh", "Srilanka")
countries2 = ("Vietnam","India","China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 31, 2, 3, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print("count of 3 in tuple1 is:", res)