from math import isqrt
def is_prime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

counter = 0
current_value = 0

while counter <= 10001:
    current_value += 1
    if is_prime(current_value):
        counter += 1

print(current_value)
