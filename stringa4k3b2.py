from Stringaaaabbbcczcount import output

s='a4k3b2'
output=''
for ch in s:
    if ch.isalpha():
        unicode = ord(ch)
        output=output+ch
    else:
        output=output+chr(int(ch)+unicode)
print("Output::",output)