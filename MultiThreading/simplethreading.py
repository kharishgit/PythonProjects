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

class new_thread(Thread):
    def run(self):
        for i in range (4):
            print("Child Thread",threading.current_thread().name)
t= new_thread()
t.start()