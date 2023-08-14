# s= 'harish is Great'
# l = s.split()
# op=[]
# for i in l:
#     op.append(i[::-1])
#
# print(' '.join(op))

# s= 'one two three four five six seven eight nine'
# l = s.split()
# length = len(l)
# print(length)
# op=[]
# for i in range(length):
#     if i%2==0:
#         op.append(l[i][::-1])
#     else:
#         op.append(l[i])
# print(' '.join(op))


# s = 'durgasoft'
# print(s[1::2])
# i=1
# print("in odd index")
# while i < len(s):
#     print(s[i],end="")
#     i+=2
import json
# #
# s="[1,10,789,3,12]"
# # print(eval(s))
# lst = json.loads(s)
# print((lst))
# # print()
# s ="7000.80"
# print(type(s))
# f =float(s)
# print(s)
# print(type(f))

# d=[]
# a=[]
# for ch in s:
#     if ch.isalpha():
#         a.append(ch)
#     else:
#         d.append(ch)
# op="".join(sorted(a)+sorted(d))
# print(op)
# import random
# from datetime import datetime
#
# string = str(datetime.now().strftime("%Y%m%d%H%M%S%z"))
# random_number = random.randint(100000, 999999)
# print(random_number)
# type="abc"
# name="ABCDhjh"
# print(type[:2])
# chk = (str(1)+type[:2]+name[:4]+str(random_number)+string).upper()
# print(chk)
# urls = "https://vimeo.com/845479102"
# index = urls.index('.com/') + len('.com/')
# numbers = urls[index:]
# print(numbers)
# num = 907
# str_num = str(num)
# lst_num=list(str_num)
# leng = len(list(lst_num))
# j=1
# for i in range(leng,0):
#     print(i)
#     # print(lst_num[i])
#     nn = lst_num[i]*j
#     print(nn)
#     j=j*
#     # print(j)
# # print(nn,end='')
# num = 123
# num = abs(num)
# print(num)
# str_num = str(num)
# lst_num = list(str_num)
# length = len(lst_num)
# j = 1
# nn=0
# for i in range(0,length):
#     nn = int(lst_num[i]) * j +(nn)
#     j = j * 10
# print(nn)
# st = "A19W8D5"
# dig=[]
# al=[]
# for ch in st:
#     if ch.isalpha():
#         al.append(ch)
#     else:
#         dig.append(ch)
# print(sorted("".join(al)+"".join(dig)))
ip = 'c2b2a4'
op=''
for ch in ip:
    if ch.isalpha():
        x=ch
    else:
        op=op+(x * int(ch))
print(''.join(sorted(op)))




