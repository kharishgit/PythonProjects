def foo(a,b,*args,**kwargs):
    print(a,b)
    for val in args:
        print(val)
    for key in kwargs:
        print(key,kwargs[key])
foo(1,2,4,5,six=6,seven=7)