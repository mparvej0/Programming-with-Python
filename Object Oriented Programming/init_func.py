class student:
    name = "karan"
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in Database.")
s1 = student("karan", 97)
print(s1.name, s1.marks) #karan

s2 = student("arjun", 88)
print(s2.name, s2.marks)

#OR
class student:
    #default constructors
    def __init__(self):
        pass
    #parameterized constructors
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks
        print("Add student in University Database.")
    s1 = student("Raju", 91)
    print(s1.name, s1.marks)
    s2 = student("Mahi", 87)
    print(s2.name, s2.marks)