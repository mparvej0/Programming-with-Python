letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Raju"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"we use f-string like this: Hey my name is {name} and I am from {country}")
price = 49.0999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format(Price = 49.0999))
# print(txt.format())
print(f"{2*30}")
print(type(f"{20*30}"))