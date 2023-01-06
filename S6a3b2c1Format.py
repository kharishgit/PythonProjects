# Print like A3B2C1 as AAABBC


val = input("Enter values")
op=''
for ch in val:
    if ch.isalpha():
        x=ch
        print (x)
    else:
        op = op + (x * int(ch))
print(op)