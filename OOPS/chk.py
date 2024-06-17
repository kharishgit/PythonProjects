class Employee:
    def __init__(self,eno,ename,esal):
        self.eno =eno
        self.esal = esal
        self.ename=ename
    def display(self):
        print("Enum =", self.eno)
        print("EName =", self.ename)

        print("ESal =", self.esal)


class Test:
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()
e=Employee(123,"Raju",10000)
Test.modify(e)
