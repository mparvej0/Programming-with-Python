info = {
    "key" : "value",
    "name" : "Raju",
    "Learning" : "Coding",
    "age" : 21,
    "is_adult" : True,
    "marks" : 87.4,
    "subjects" : ["Python", "Java", "C++", "JavaScripts"],
    "topics" : ("dict", "set"),
    12.99 : 94.44,
    17 : 33

}
print(info)
#OR
print(info["name"])
info["name"] = "Parvej" #Change value
info["surname"] = "Md" #Add key value pair
print(type(info))

null_dict = {}
null_dict["name"] = "Adiba Maher"
print(null_dict)

#Nested Dictionary
student = {
    "name" : "Mr. Raju",
    "subjects" : {
        "Mathematics" : 97,
        "Computer-Science" : 98,
        "Finance" : 95
    }
}
print(student)
print(student["subjects"]["Finance"])
