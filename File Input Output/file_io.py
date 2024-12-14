f= open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

#Reading
f1 = open("demo.txt", "r")
data = f1.read(5)
print(data)
f1.close()

f2 = open("demo.txt", "r")
line = f2.readline()
print(line)
f2.close()

#Writing
f3 = open("demo.txt", "w") #change data
f3.write("I want to learn Java tomorrow. 123")
f3.close()

f5 = open("demo.txt", "a")
f5.write("Then I'll move to ReatJS") #add data
f5.write("\nAfter that nodejs") #add data in next line
f5.close()

f6 = open("sample.txt", "w") #create a sample file
f6.close()