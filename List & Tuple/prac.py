movies = []
mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2nd movie: ")
mov3 = input("Enter 3rd movie: ")
    #OR
mov4 = input("Enter 4th movie: ")
movies.append(mov4)
        #OR
movies.append(input("Enter 5th movies: "))


movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

list1 = [1, 2, 1]
list2 = ["m", "a", "a", "m", "p"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Plaindrome")
else:
    print("No Plaindrome")

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

cha = ["C", "D", "A", "A", "B", "B", "A"]
cha.sort()
print(cha)