dic = {
    "Harry": "Human being", "Spon": "Object"

}

print(dic["Harry"])

dic = {
    344: "Harry",
    56: "Shubham", 
    678: "Zakir",
    567: "Neha"
}
print(dic[567])

info = {"name":"Karan", "age":19, "eligible":True}
print(info)
# print(info["name"2])
print(info.get("name2"))
print(info.keys())

for key in info.keys():
    print(info[key])
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")