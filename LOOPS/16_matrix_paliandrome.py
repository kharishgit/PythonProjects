n=3
matrix=[]
for i in range(n):
    row=[]
    for j in range(n):
        element = int(input(f"Enter elements of {i+1} th row and {j+1} column"))
        row.append(element)
    matrix.append(row)
should_exit = False
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n-1-i][n-1-j]:
            print("Not a palindrome matrix")
            should_exit=True
            break
        if should_exit:
            break
if not should_exit:
    print("Palindrome matrix")



