lst = ["apple","banana","cherry"]
lst[1:2]=['Guaca','Tomato']
print(lst)
lst.insert(1,'Orange')
print(lst)
tup = ('kiwi','banana')
lst.extend(tup)
print(lst)
lst2=['maaga','poovan pazham']
lst=lst+lst2
print(lst)
sorted(lst)
print(lst)
lst2 = [1,2,3,4]
lst22 = [i*i for i in lst2]
print(lst22)