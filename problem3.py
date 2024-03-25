import math

def temp(n):
    for i in range(2, n):
        if (n % i == 0):
            return temp(int(n / i))
    return n

print(temp(600851475143))