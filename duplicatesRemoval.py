# s='dsfnnvcbvbbddhasjdbdbfbajhasjhvv'
# op=''
# for i in s:
#     if i not in op:
#         op=op+i
# print(op)


def remove_duplicates(string):
  i = 0
  while i < len(string):
    if string[i] in string[:i]:
      string = string[:i] + string[i+1:]
    else:
      i += 1

  return string

print(remove_duplicates('sdfjnfdjweifjnfdjbfbsdfsd'))


# s='dsfdsfsdadfedfvhfgjdfsferjhv'
# print("".join(set(s)))