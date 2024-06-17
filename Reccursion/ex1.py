def reccursive_function(n):
    if n<0:
        print("n is less than 0")
    else:
        reccursive_function(n-1)
        print(n)

reccursive_function(4)