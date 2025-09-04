# def factorial(n):
#     assert n>=0 and  int(n)==n, 'The number must be positive integer'
#     if n in [0,1]:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# try:
#     print(factorial(3))
# except Exception as e:
#     print(e)

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
test_cases = [0, 1, 3, 5]
for n in test_cases:
    print(f"Input: n={n}, Output: {factorial(n)}")