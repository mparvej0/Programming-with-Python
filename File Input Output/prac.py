with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

#Replace
with open("practice.txt", "r") as f1:
    data = f1.read()
new_data = data.replace("Java", "Python")
print(new_data)
with open("practice.txt", "w") as f1:
    f1.write(new_data)

#Searching word in file
word = "learning"
with open("practice.txt", "r") as f2:
    data = f2.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")
#OR
def check_for_word():
    word = "learning"
with open("practice.txt", "r") as f2:
    data = f2.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")
check_for_word()

def check_for_line():
    word = "learng"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f3:
        while data:
         data = f3.readline()
         if(word in data):
             print(line_no)
             return
        line_no += 1
        return -1
    print(check_for_line())

    count = 0
    with open("data_prac.txt", "r") as f4:
        data1 = f4.read()
        nums = data1.split(",")
        for val in nums:
            if(int(val) % 2 == 0):
                count += 1
            print(count)