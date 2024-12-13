collection = set()
collection.add(1)
collection.add(2)
collection.add("Soas University of London")
collection.add((3, 4, 5))
print(collection)
print(len(collection))

collection1 = set()
collection1.add(3)
collection1.add(4)
collection1.remove(4)
print(collection1)

collection.clear()
print(len(collection))

collection2 = {"Hello", "IITM", "World", "Coding", "Python"}
print(collection2.pop())
print(collection2.pop())

set = {1, 2, 3}
set1 = {2, 3, 4}
print(set.union(set1)) #{1, 2, 3, 4}

se2 = {1, 2, 3}
set3 = {2, 3, 4}
print(se2.intersection(set3)) #{2, 3}