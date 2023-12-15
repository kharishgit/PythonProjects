class Student:
    collegename="Durga"
    director = "Harish"
    def __init__(self,name,age,location):
        print(id(self))
        self.name = name
        self.age= age
        self.location = location
    def talk(self):
        self.ckk="ABC"
        print("my name is :",self.name)
        print("my age is :",self.age)
        print("my location is :",self.location)
    @classmethod
    def collegeinfo(cls):
        print("Collage Name:",Student.collegename)
        print("Director:",Student.director)



s=Student("Kumari",67,"Kuttippuram")
print(s.__dict__)
print(s.name,s.age,s.location)
Student.collegeinfo()
print(Student.collegename)
print(id(s))
s.talk()
print(s.__dict__)


# class Hello:
#     print("Hii")
# h=Hello()
# print(h)