n=3
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for k in range(1,n):
    for j in range(k):
        print(" ",end=" ")
    for j in range(2 * (n - k) - 1):
        print("*",end=" ")
    print()