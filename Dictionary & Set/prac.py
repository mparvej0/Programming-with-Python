dict = {
    "Cat" : "A small animal",
    "Table" : ["A piece of furniture", "List of facts & figures"]
}
print(dict)

sub = {
    "Python", "Java", "C++", "Python", "JavaScript", "Java", "Python", "Java", "C++", "C"
}
print((len)(sub))

marks = {}
x = int(input("Enter Physics :"))
marks.update({"Physics" : x})
x = int(input("Enter Mathematics :"))
marks.update({"Mathematics" : x})
x = int(input("Enter Chemistry :"))
marks.update({"Chemistry" : x})
print(marks)

values = {9, "9.0", 9.0, 9.25, 8, 8.0}
print(values)
#OR
values1 = {
    ("float", 9.0),
    ("int", 9)
}
print(values1)