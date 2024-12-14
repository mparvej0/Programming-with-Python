with open("syntax.txt", "r") as f:
    data = f.read()
    print(data)

with open("syntax.txt", "w") as f:
    f.write("new data")