n= int(input("Enter rows"))
for i in range(n):
    print(' '  * (n-i-1),end="")
    for j in range(i+1):
        print((n-j),end=" ")
    print()

# n=int(input("Emter"))
# for i in range(n):
#     print(' '*(n-i-1),end="")
#     for j in range(i+1):
#         print(str(n-j)+' ',end="")
#     print()