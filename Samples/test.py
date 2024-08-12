# def greet():
#     print("Hiii")
# def display(other_fun):
#     print("This is display function")
#     greet()
# display(greet)

# def outer():
#     print("Outer function")
#     def inner():
#         print("Inside inner")
#     print("Returning ")
#     return inner
# f=outer()
# f()

# def generator(val):
#     while val>0:
#         yield val
#         val= val-1
# count = generator(10)
# for i in count:
#     print(i)

# s = "durgasoft"
# print(s[1::2])

# s= "aaaabbbffz"
# lst = list(s)
# print(lst)
# set1 = set(lst)
# print(set1)
# lst2=list(set1)
# print(lst2)
# for ch in sorted(lst2):
#     print(ch+str(lst.count(ch)),end="")

# def foo(a,b, *arg,**kwargs):
#     print(a,b)
#     for i in arg:
#         print(i)
#     for key in kwargs:
#         print(key, kwargs[key])
# foo(1,2,3,4,5,six=6,seven=7)


def recfun(n):
    if n < 1:
        print("Num is < n")
    else:
        recfun(n-1)
        print(n)
recfun(4)