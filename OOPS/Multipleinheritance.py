class Human:

    def work(self):
        print("working")
class Man:


    def work(self):
        # super().work()
        print("woking differently")


class Boy(Human,Man):
    def work(self):
        # super().work()
        print("Working as boy")

b=Boy()
b.work()
Human.work(b)
print(Boy.mro())