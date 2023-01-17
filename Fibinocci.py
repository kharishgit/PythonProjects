def fib(limit):
    a,b=0,1
    i=0
    while i < limit:
        print(a)
        a,b=b,b+a
        i+=1
    # return b
print(fib(7))

# def fibbinocci(limit):
#     if limit<=0:
#         return 0
#     elif limit==1:
#         return 1
#     else:
#         return fibbinocci(limit-1)+fibbinocci(limit-2)
# print(fibbinocci(1))