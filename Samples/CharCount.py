s="ABCBBSJSBABSBASCAFBCBD"
new=[]
for ch in s:
    if ch not in  new:
        new.append(ch)
        cnt=s.count(ch)
        print(f'The val {ch} occurs{s.count(ch)} times')