def deco(func):
    def wrapper(*args,**kwargs):
        print("Start")
        res=func(*args,**kwargs)
        print(res)
        print('Working')
    return wrapper

@deco
def display():
    print('Middle')

display()

@deco
def calc(x,y):
    return x+y
calc(12,13)





# def decorate(func):
#     def add(a,b):
#         result = func(a+b)
#         return result
#     return add
#
#
# @decorate
# def double(x):
#     return 2*x
#
# print(double(3,4))