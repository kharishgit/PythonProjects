import threading
from threading import *
# def display():
#     for i in range(10):
#         print("Child Thread")
# t= Thread(target=display)
# t.start()
# for i in range(5):
#     print("Main Thread")

###### USING CLASSES ##

# class new_thread(Thread):
#     def run(self):
#         for i in range (4):
#             print("Child Thread",threading.current_thread().name)
# t= new_thread()
# t.start()

def buble(lst):
    for i in range (len(lst)):
        for j in range (0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst
sort = buble([3,5,12,6,4])
print(sort)
