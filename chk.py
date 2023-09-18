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

def my_dec(func):
    def wrapper(*args,**kwargs):
        print("before")
        result =func(*args,**kwargs)
        print("after")
        return result
    return wrapper

@my_dec
def hello(a,b):
    return a+b
print(hello(10,13))











