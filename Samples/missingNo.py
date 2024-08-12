def missing_no(n):
    for i in range(1,len(n)+1):
        if i not in n:
            return i

print(missing_no([-8,-7,-6]))