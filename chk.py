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


ip=[1,7,2,15]
target = 9
for i in ip:
    rem = target - i
    ind1 = ip.index(rem)
    if ind1:
        print(ip.index(i),ind1)
        break
















