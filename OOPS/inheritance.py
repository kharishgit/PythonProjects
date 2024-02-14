class Human:
    def __init__(self):
        self.eyes =2
        self.mouth = 2
    def talk(self):
        print("Talking")
    def work(self):
        print("working")
class Man(Human):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def work(self):
        super().work()
        print("woking differently")
    def display(self):
        print(f"the name is {self.name}")

m = Man("Hari")
m.talk()
m.work()
print(m.eyes)
m.display()