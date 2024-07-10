# def reccursive_function(n):
#     if n<1:
#         print("n is less than 1")
#     else:
#         reccursive_function(n-1)
#         print(n)
#
# reccursive_function(4)

def power_of_two(n):
    if n==0:
        return 1
    else:
        power_of_two(n-1)
        return n**2
res=power_of_two(4)
print(res)