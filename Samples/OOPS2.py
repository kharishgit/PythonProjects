class Test:
    x = 10
    def __init__(self):
        self.y = 20
    @classmethod
    def m1(cls):
        cls.x=555
        cls.y=666

t1= Test()
print(t1.x,t1.y)
t1.x=333
t1.y = 222
print("After changes",t1.x,t1.y)

t2=Test()
print("T2",t2.x,t2.y)
t3=Test()
t3.m1()
print("T3",t3.x,t3.y)
