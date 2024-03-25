number = 6006

def is_palindrome(n):
    snumber = str(n)
    first_half = (snumber[:int(len(snumber)/2)])
    second_half = snumber[int(len(snumber)/2):]
    if (first_half[::-1] == second_half):
        return True
    else:
        return False

def largest_palindrom():
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if (is_palindrome(i*j) and i*j > largest):
                largest = i*j
    return(largest)
print(largest_palindrom())