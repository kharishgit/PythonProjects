n=4
for i in range(n):
    for j in range(i+1):
        print((i+1)-j,end=" ")
    print()



def print_reverse_number_pattern(n):
    # Outer loop for rows
    for i in range(1, n + 1):  # Rows 1 to n
        # Inner loop for numbers from i down to 1
        for j in range(i, 0, -1):  # Count down from i to 1
            print(j, end=" ")  # Print number with space
        print()  # New line after each row

# Test the function
n = 4
print_reverse_number_pattern(n)