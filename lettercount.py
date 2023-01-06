s='sdfdsvds'
res={}

for ch in s:
    if ch not in res:
        res[ch]=1
    else:
        res[ch]+=1
print(res)
