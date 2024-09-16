i = [3, 5, 6]
print(i)
print(type(i))

marks = [3, 5, 6, "Harry", True, 6, 7, 2, 32, 345, 23]
print(marks)
print(marks[:])
print(marks[0:len(marks)])
print(marks[1:-1])
print(marks[1:8])
print(marks[1:4:3])
print(marks[0:7])
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

# Converting negative index to postive
print(marks[-3]) # Negative index
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index

# i want know 7 availabe on list
if 7 in marks:
# if "Harry" in marks:
    print("Yes")
else:
    print("No")

if "arry" in "Harry":
    print("Yes")

lst = [(i for i in range(4))]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

l = [11, 45, 1, 2, 4, 6]
print(l)
# l.append(7)
# l.sort()
# l.sort(reserve=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()
# m = l
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
print(k)
l.extend(m)
print(l)
