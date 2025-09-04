def fib_naive(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib(n):
    hash = {}
    def fib_helper(n):
        if n in hash:
            return hash[n]
        if n==0:
            return 0
        if n==1:
            return 1
        hash[n] = fib_helper(n-1) + fib_helper(n-2)
        return hash[n]
    return fib_helper(n)

test_cases = [0, 1, 2, 5]
for n in test_cases:
    print(f"Input: n={n}, Output (Naive): {fib_naive(n)}, Output (Memoized): {fib(n)}")