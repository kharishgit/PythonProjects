# from abc import ABC , abstractmethod
# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass
# class Laptop(Computer):
#     def process(self):
#         print("Running")
#
# class Programmer():
#     def work(self,com):
#         print("Fix bug")
#         com.process()
#
#
# class WhiteBoard(Computer):
#     def write(self,com):
#         print("Writing")
#         com.process()

# com=Computer()
# com.process()
# lap=Laptop()
# lap.process()
# prg=Programmer()
# prg.work(lap)
# wb=WhiteBoard()
# wb.write()
# from datetime import datetime, timedelta
#
# borrowed_on = '2023-07-18'
# duedate = 7
# borrowed_on_date = datetime.strptime(borrowed_on, '%Y-%m-%d').date()
# duedate = borrowed_on_date + timedelta(days=duedate)
# print(duedate)
# current_date = datetime.today().strftime('%Y-%m-%d')
# print(current_date)
# from datetime import datetime, timedelta
#
# borrowed_on = '2023-07-18'
# duedate = 7
# borrowed_on_date = datetime.strptime(borrowed_on, '%Y-%m-%d').date()
# duedate = borrowed_on_date + timedelta(days=duedate)
#
# current_date = datetime.today().date()
# print (current_date)
# difference = duedate - current_date
# number_of_days = difference.days
#
# print("Number of days until the due date:", number_of_days)
#
#
# print("Number of days until the due date:", number_of_days)

# target = 7
# lst = [2,3,1,2,4,3]
# print(len(lst))
# for i in range(0,len(lst)):
#     big = max(lst)
#     num = target-big
#     res=[]
#     # try:
#     #     r=lst.index(num)
#     # except:
#     #     pass
#     if big <= target:
#         res.append(big)
#         print(big)
#         # while big in lst:
#         #     lst.remove(big)



# d={}
# d['A']=100
# d['B']=200
# d['A']=300
# d['B']=d.get('B',0)+1
# for k,v in sorted(d.items()):
#     print(k,v)

# lst = [1,2,3,4,5]
# lst2=[i*i for i in lst]
# print(lst2)

# mydict = dict(name="hai",age=50,address="kuttippuram")
# print(''.join(map(str,list(mydict.values()))))


# s="abcd"
# print(s[::-1])
# print(''.join(reversed(s)))
#
# op=''
# l=len(s)-1
# for i in range(l+1):
#     op=op+s[l-i]
# print(op)

# def my_dec(func):
#     def wrapper(*args,**kwargs):
#         print("before")
#         result =func(*args,**kwargs)
#         print("after")
#         return result
#     return wrapper
#
# @my_dec
# def hello(a,b):
#     return a+b
# print(hello(10,13))


# def fib(limit):
#     a,b = 0,1
#     i=0
#     fibinocci_series=[]
#     while i <limit:
#         fibinocci_series.append(a)
#         a,b = b,a+b
#         i+=1
#     return fibinocci_series
#
# print(fib(8))

# add = lambda x,y:x+y
# result = add(3,4)
# print(result)

# numbers = [1,2,3,4,5]
# square = map(lambda x:x*x,numbers)
# print(list(square))

# numbers = [1,5,23,45,65,78]
# div_by_five = filter(lambda x:x%5==0,numbers)
# print(list(div_by_five))

# set_chk = set("Hello")
# print(len(set_chk))
import time
# s=" harish is the prime minister of india"
# l=s.split()
# for i in range (len(l)):
#     if i% 2==0:
#         print(l[i],end=" ")
#     else:
#         print(l[i][::-1],end=" ")
#
# l1 = ['a', 'b', 'c', 'd', 'e', 'f']
# l2 = [1, 2, 3, 4, 5, 6, 7]
#
# # Concatenating lists
# l3 = l1 + l2
# print(sorted(l1)+sorted(l2))
# s='aaaa'
# op=''
# previous = s[0]
# c=1
# i=1
# while i <len(s):
#     if s[i]==previous:
#         c+=1
#     else:
#         op = op + str(c)+previous
#         previous=s[i]
#         c=1
#     if i==len(s)-1:
#         op = op+ str(c)+previous
#     i=i+1
# print(op)
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s=str(x)
#         if s==s[::-1]:
#             return True
#         else:
#             return False
# s=Solution()
# res=s.isPalindrome(121)
# print(res)
# d={}
# d['A'] = 100
# print(d)
# d['A']=300
# d['B']=111
# print(d)
# print(d.get('A'))
# d['A']=(d.get('A')+1)
# print(d)


# lst=[1,2,3,4,5]
# lst2=[i*i for i in lst]
# print(lst2)

# dic = {"name":"Harish","age":"41","city":"kuttippuram"}
# # dic.popitem()
# print(dic)
#
# val = dic["name"]
# print(val)

# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]):
#         w1op=''
#         w2op=''
#         for ch in word1:
#             w1op =  w1op+ch
#         for ch in word2:
#             w2op =  w2op+ch
#         if w1op == w2op:
#             return True
#         else:
#             return False



# def min(lis):
#     return sorted(lis)[0]
#
# li = [4,5,6,8,1,2,3]
# print(min(li))

# from collections import Counter
# a='aaasssdasrreweewhyeyeyuuuueyttytettharish'
# values=Counter(a)
# for k,v in values.items():
#     print(f"key= {k} and value={v}")

# s="hai how are yoiu"
# t=list(s)
# print(s.split('y'))

# def disp(n):
#     if n>0:
#         disp(n-1)
#     print(n)
# disp(10)

# print("hiii")
# print(__name__)
#
#
#
#
#
# def disp(n):
#     if n>0:
#         disp(n-1)
#     print(n)
#
# disp(10)


# def fib(limit):
#     a,b =0,1
#     while a<limit:
#         yield a
#         a,b = b,a+b
# f=fib(10)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# def gen(limit):
#     while limit >= 0:
#         yield limit
#         limit-=1
# x=gen(10)
# for i in x:
#     print(i)
# a="123456789"
# print(a[:4])
# v1 = input("V1")
# v2 = input("V2")
# def compare(v1,v2):
#     # print(v1,v2)
#     ver1 = "".join(v1.split('.'))
#     ver2 = "".join(v2.split('.'))
#     version1 = "".join(ver1.split('0'))
#     version2 = "".join(ver2.split('0'))
#
#     print(version1,version2)
#
#
# compare(v1,v2)
# try:
#     x= int(input("Enter num"))
#     y = int(input("Enter sec num"))
#     print(x/y)
# except Exception as e:
#     print(e)

# import math
#
# def is_prime(number):
#     if number <= 1:
#         return False
#     if number <= 3:
#         return True
#     if number % 2 == 0 or number % 3 == 0:
#         return False
#     sqrt_num = int(math.sqrt(number))
#     print(sqrt_num)
#     for i in range(5, sqrt_num + 1, 6):
#         print("I:",i)
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#     return True
#
# # Test the function
# number = 31  # Change this number to test different values
# if is_prime(number):
#     print(f"{number} is a prime number")
# else:
#     print(f"{number} is not a prime number")

# def leap_year(year):
#     if year%4==0:
#         return True
#     return False
# def get_days(year,month):
#     days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if leap_year(year) and month==2:
#         return 29
#     else:
#         return days_list[month-1]
# print(get_days(2005,8))
# def greet_loader(name):
#     print(f"Hi {name.upper()}")
# def greet_softer(name):
#     print(f"Hi {name.lower()}")
# def hello(other_fun,name):
#     print("This is from hello")
#     other_fun(name)
# hello(greet_loader,"harish")

# def hello(name):
#     print("From hello")
#     def greet():
#         print("From Greet")
#     def welcome():
#         print("From Welcome")
#     if name=="Harish":
#         return greet
#     return welcome
# new_fun=hello("Harsh")
# new_fun()
# def add(x,y):
#     print("from add")
#     return x+y
# def sub(x,y):
#     return x-y
# def calculate(other_fun,x,y):
#     res=other_fun(x,y)
#     return res
#
# result=calculate(add,3,4)
# print(result)
# s= "hello"
# print(s.replace('l','L'))
# print(s)
# def deco(fun):
#     def wrapper(c,d):
#         print("start")
#         result=fun(c,d)
#         print("End")
#         return result
#     return wrapper
#
# @deco
# def check(a,b):
#     return a+b
# print(check(3,4))
# def fib(num):
#     a,b=0,1
#     while num > a:
#         yield a
#         a,b=b,a+b
#
# g=fib(20)
# for i in g:
#     print(i)

# class Duck:
#     def swim(self):
#         print("I can Swim in water")
#     def talk(self):
#         print("Qack! I can")
# class Dog:
#     def swim(self):
#         print("I can Swim in water with my legs")
#     def talk(self):
#         print("Bark! I can")
#
# def display(duck):
#     duck.swim()
#     duck.talk()
#
# d=Duck()
# dog=Dog()
# display(dog)
# s="ABAABBCCGGJHGHJ"
# d={}
# for ch in s:
#     d[ch]=d.get(ch,0)+1
# for k,v in sorted(d.items()):
#     print(f"{k} occurs {v} times")
# s="AJISIIOEHNNCHEYTEU"
# v=['a','e','i','o','u']
# d={}
# for ch in s.lower():
#     if ch in v:
#         d[ch]=d.get(ch,0)+1
# print(d)
# class Demo:
#     def add(self,*args):
#         res=0
#         for i in args:
#             res=res+i
#         return res
# d=Demo()
# print(d.add(3,4,5))
# print(d.add(30,23,9,4,5))

# class Book:
#     def __init__(self,pages):
#         self.pages = pages
#
#     def __str__(self):
#         return str(self.pages)
#
#     def __add__(self,other):
#         total=self.pages+other.pages
#         b=Book(total)
#         return b
#
# b1=Book(100)
# b2=Book(400)
# b3=Book(300)
# b4=Book(300)
# print(b1+b2+b3+b4)

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary= salary
#
# class TimeSheet:
#     def __init__(self,name,time):
#         self.name = name
#         self.time= time
#
#     def __mul__(self, other):
#         return self.time * other.salary
# e=Employee("Durga",500)
# t= TimeSheet("Durga",30)
# print(t*e)

# class Test:
#     def sum(self,*args):
#         total =0
#         for i in  args:
#             total= total+i
#         print(total)
# t=Test()
# t.sum(3,4,5)
# t.sum(3,4,5,6,6,7,8)
# from threading import *
# class Mythread(Thread):
#     def run(self):
#         for i in range(10):
#             print("child")
# t=Mythread()
# t.start()
# for i in range(10):
#     print("Main")

# def sum(x,y):
#     try:
#         result = x/y
#         return result
#     except ZeroDivisionError:
#         print("Y=0 is not allowed")
#         return f"Y=0"
# print(sum(4,0.1))
#

# from threading import *
# import time
# def display():
#     for i in range(10):
#         print("Child thread")
# time.sleep(3)
#
# t=Thread(target=display)
# t.start()
# # t.join(3)
# for i in range(10):
#     print("Main")
#     # time.sleep(.5)

# class Car:
#     def __init__(self,make,model,year):
#         self._make = make
#         self.__model = model
#         self.__year=year
#
#     def set_make(self,make):
#         self._make=make
#     def get_model(self):
#         return self.__model
#     def set_year(self,year):
#         self.__year =year
#
#     def display(self):
#         return f"Model is {self.__model} Make is {self._make} year is {self.__year}"
#
# c=Car("Toyota","Altis",2000)
# c.set_make("Maruthi")
# print(c.display())
# print(c.get_model())
# c.set_year(2020)
# print(c.display())

# print("Hiii")
# if __name__ == '__main__':
#     print("This is only for chk")

# def louder(name):
#     print(f"hii {name.upper()}")
# def display(other_fun,name):
#     print("Hello")
#     other_fun(name)
# display(louder,"Jenny")
