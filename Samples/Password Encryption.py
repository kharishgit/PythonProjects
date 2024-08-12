# Company decided to set encryption for user typed password.
# The Alphabetic order is cyclic and the encription is based on the
# Kth number inputed by user.







str1=input("Enter Password")
k=int(input("Enter Key"))
lst=[]
for i in str1:
    ask = ord(i)
    if ask>=122:
        ask=ask-26
    lst.append(ask)
# print(lst)
res = [x + k for x in lst]
# print(res)
lst2=[]
for i in res:
    pswd = chr(i)
    lst2.append(pswd)
print(''.join(lst2))




