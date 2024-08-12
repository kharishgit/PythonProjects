s1='abcdefgh'
s2='lmno'
s3='xz'
i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    op=''
    if i<len(s1):
        op=op+s1[i]
        i=i+1
    if j<len(s2):
        op=op+s2[j]
        j=j+1
    if k<len(s3):
        op=op+s3[k]
        k=k+1
    print(op)
