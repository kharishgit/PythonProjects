# Design an algorithm to encode a list of strings into a single string and then decode it
# back to the original list of strings. The encoded string should be reversible, meaning you can uniquely
# reconstruct the original list from it.
# Example:
#
# Input: ["Hello", "World"]
# Encode: "5#Hello5#World"
# Decode: ["Hello", "World"]
# Explanation: Each string is prefixed with its length and a delimiter (e.g., #) to separate it from others.
#
# Constraints:
#
# 0 <= strs.length <= 10^4
# 0 <= strs[i].length <= 10^3
# strs[i] can contain any printable ASCII characters (including # or numbers).
# You can assume the encoded string can be transmitted and decoded correctly.







class Codec:
    def encode(self, strs):
        # Encode each string as "length#string" and join them
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        # Decode the single string back to a list of strings
        result = []
        i = 0
        while i < len(s):
            # Find the length (digits before '#')
            length = 0
            while i < len(s) and s[i].isdigit():
                length = length * 10 + int(s[i])
                i += 1
            # Skip the '#' delimiter
            i += 1
            # Extract the string of given length
            result.append(s[i:i + length])
            i += length
        return result


# Test it
codec = Codec()
strs = ["Hello", "World"]
encoded = codec.encode(strs)
print(encoded)  # "5#Hello5#World"
decoded = codec.decode(encoded)
print(decoded)  # ["Hello", "World"]