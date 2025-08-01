def is_prime(n):
    if n<=1:
        return False
    count = 0
    for i in range(2,n//2):
        if n%i==0:
            count+=1
    if count>=1:
        return False
    return True
print(is_prime(9))



def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # Check even numbers (except 2)
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # Check odd numbers up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(9))     # Output: False
print(is_prime(17))    # Output: True
print(is_prime(2))     # Output: True
print(is_prime(1))     # Output: False