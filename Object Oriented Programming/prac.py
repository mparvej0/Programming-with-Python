class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your ave score is:", sum/3)
s1 = student("Tony Stark", [99, 98, 97])
s1.get_avg()
s1.name = "Ironman" #chang value
s1.get_avg()

class Account :
    def __init__(self, bal ,acc):
        self.balance = bal
        self.account_no = acc
    def debit(self, amount): #debit method
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())
    def credit(self, amount): #creit method
         self.balance += amount
         print("Rs.", amount, "was credited")
    def get_balance(self):
        return self.balance
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
print(acc1.balance)
print(acc1.account_no)