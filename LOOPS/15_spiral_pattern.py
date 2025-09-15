n=4
grid = [[0 for _ in range(n)]for _ in range(n)]
top,bottom,left,right = 0, n-1,0,n-1
num=1
while top<=bottom and left<=right:
    for j in range(left,right+1):
        grid[top][j]=num
        num+=1
    top+=1
    for i in range(top,bottom+1):
        grid[i][right]=num
        num+=1
    right-=1
    if top<=bottom:
        for j in range(right,left-1,-1):
            grid[bottom][j]=num
            num+=1
        bottom-=1
    if left<=right:
        for i in range(bottom, top-1,-1):
            grid[i][left]=num
            num+=1
        left+=1

for i in range(n):
    for j in range(n):
        print(grid[i][j],end=" ")
    print()