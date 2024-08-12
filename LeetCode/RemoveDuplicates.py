s="abcdczbba"
op=''
for ch in s:
    if ch not in op:
        op=op+ch
print(op)

#####Other Methods###########
rem_dup = []
for ch in s:
    if ch not in rem_dup:
        rem_dup.append(ch)
print("".join(rem_dup))



#######Other Method######
s1=set(s)
print("".join(sorted(s1)))