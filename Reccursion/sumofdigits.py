# def sum_of_digits(n):
#     if n==0:
#         return 0
#     else:
#
#         return int(n%10)+sum_of_digits(n//10)
#
#
# print(sum_of_digits(1235))

def sum_to_n(n):
    if n==0:
        return 0
    else:
        return n+sum_to_n(n-1)

test_cases = [0, 1, 3, 4]
for n in test_cases:
    print(f"Input: n={n}, Output: {sum_to_n(n)}")