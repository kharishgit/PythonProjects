# def greet():
#     print("Hiii")
# def display(other_fun):
#     print("This is display function")
#     greet()
# display(greet)

s="Learning Python is very easy"
# d = {}
# for ch in s:
#     d[ch] = d.get(ch,0)+1
# for k,v in sorted(d.items()):
#     print(f"{k} is occured {v} times")
l= s.split()
for i in range(len(l)):
    if i%2==0:
        print(l[i], end=" ")
    else:
        print(l[i][::-1], end=" ")
