str1 = input("Enter letters & digits")
lst=sorted(str1)
print(lst)
dig=[]
let=[]
for ch in lst:
    if ch.isalpha():
        let.append(ch)
    else:
        dig.append(ch)
print("".join(let+dig))