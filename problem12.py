def number_of_factors(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count

current_number = 76576500
iteration = 0
while number_of_factors(current_number) <= 500:
    iteration += 1
    current_number += iteration
    print(current_number)

print(current_number)
