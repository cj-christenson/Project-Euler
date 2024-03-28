max_value = 2000000
current_prime = 2
total = 0
list_of_ints = [True] * max_value
list_of_ints[0] = False

while current_prime < max_value : #implementation of Sieve of Eratosthenes
    if (list_of_ints[current_prime - 1]):
        for i in range(current_prime*2, max_value+1, current_prime):
             list_of_ints[i-1] = False
    current_prime += 1

for index in range(len(list_of_ints)):
    if (list_of_ints[index]):
        total += (index + 1)

print(total)