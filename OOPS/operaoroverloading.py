class Billing:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

b1=Billing('Hari',4)
b2=Billing('Aadi',35)
if b1>b2:
    print(f"{b1.name } will pay" )
else:
    print(f"{b2.name } will pay" )

