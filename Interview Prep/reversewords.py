def reverse_words(s):
    stack = s.split()
    nstack = []
    for wrd in stack:
        nstack.append(wrd)
    return " ".join(nstack[::-1])
print(reverse_words("hello world python"))


## Optimal Solution

def reverse_word(s):
    word = s.split()
    word.reverse()
    return " ".join(word)
print(reverse_words("hello world python"))