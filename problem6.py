def sum_of_squares(max):
    sum = 0
    for i in range(1, max+1):
        sum += i**2
    return sum
def squares_summed(max):
    
    sum = 0
    for i in range(1, max+1):
        sum += i
    sum **= 2
    return sum
print(squares_summed(100) - sum_of_squares(100))