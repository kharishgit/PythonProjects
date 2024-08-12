# dict={
#     '(':')',
#     '[' : ']',
#     '{' : '}'
# }
# s = input("Enter String")
# for k,v in dict.items():
#     if k in s and v in s:
#         print(True)
#     else:
#         print(False)

import threading

# Subclassing Thread class
class MyThread(threading.Thread):
    def run(self):
        print("Thread running")

# Creating and starting a thread
my_thread = MyThread()
my_thread.start()
