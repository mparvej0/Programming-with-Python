student = {
    "name" : "Mr. Raju",
    "subject" : {
        "phy" : 87,
        "che" : 92,
        "math" : 79
    }
}
print(student.keys())
            #OR
print(list(student.keys()))
            #OR
print(len(list(student.keys())))
            #OR
print(len(student))

print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))

pairs = list(student.items())
print(pairs[0])

print(student["name"])
        #OR
print(student.get("name"))

student.update({"City" : "Delhi"})
            #OR
new_dict = {"City" : "Delhi"}
student.update(new_dict)
print(student)
