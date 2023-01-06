#Get the number of '-' or '|' needed to print the Numbers
string='1234123'
val={
    '1':2,
    '2':5,
    '3':10,
    '4':6
}
cnt=0
for i in string:
    cnt+=val[i]
print(cnt)
