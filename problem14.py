def even(n):
    return (n/2)

def odd(n):
    return (3*n + 1)

def length_collatz(n):
    counter = 1
    while n != 1:
        if n % 2 == 0:
            n = even(n)
            counter += 1
        else:
            n = odd(n)
            counter += 1
    return counter

largest_collatz = 0
longest_length = 0
for i in range(1,1000000):
    length = length_collatz(i)
    print(i, length)
    if length > longest_length:
        longest_length = length
        largest_collatz = i
print(largest_collatz)
