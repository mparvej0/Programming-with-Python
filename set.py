s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

Raju = set()
print(type(Raju))

for value in info:
    print(value)

# Merge
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

cities = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Tokyo","Seol","Kabul", "Madrid"}
cities3 = cities.union(cities2)
cities.intersection_update(cities2)
cities3 = cities.symmetric_difference(cities2)
cities.add("Helsinki")
cities.discard("Tokyo2")
item = cities.pop()
print(item)
# del cities
print(cities.isdisjoint(cities2))
print(cities.issuperset(cities2))
print(cities.issuperset(cities3))
print(cities.issubset(cities3))
print(cities3)
print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")