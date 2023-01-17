s='abcdd'
op=''
prv = s[0]
i=1
cnt=1
while i < len(s):
    if s[i] == prv:
        cnt+=1
    else:
        op=op+str(cnt)+prv
        prv = s[i]
        cnt=1
    if i== len(s)-1:
        op=op+str(cnt)+prv
    i+=1
print(op)