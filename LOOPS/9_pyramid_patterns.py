n= int(input("enter the rows"))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    for j in range(i):
        print("*",end=" ")
    print()



def print_pyramid(n):
    # Outer loop for rows
    for i in range(1, n + 1):  # Rows 1 to n
        # Inner loop for spaces
        for j in range(n - i):  # Print n-i spaces
            print(" ", end=" ")
        # Inner loop for stars
        for j in range(2 * i - 1):  # Print 2*i-1 stars
            print("*", end=" ")
        print()  # New line after each row

# Test the function
n = 3
print_pyramid(n)