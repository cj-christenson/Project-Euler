a = 0
b = 1
sum = 0
while a <= 4000000:
    b, a = a + b, b
    if (a % 2 == 0):  
        sum += a
    

print(sum)