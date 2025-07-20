def word_frequency(s):
    freq={}
    word_list = list(s.split())
    for word in word_list:
        freq[word]=freq.get(word,0)+1
    return freq


s = "apple banana apple orange banana"
print(word_frequency(s))



def word_frequency(s):
    freq = {}
    for word in s.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

# Test cases
print(word_frequency("apple banana apple orange banana"))  # Output: {'apple': 2, 'banana': 2, 'orange': 1}
print(word_frequency("hello"))                             # Output: {'hello': 1}
print(word_frequency(""))