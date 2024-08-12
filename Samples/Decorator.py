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


