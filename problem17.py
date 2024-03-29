from num2words import num2words

def char_num(n):
    number = num2words(n)
    number = number.replace(' ', '')
    number = number.replace('-', '')
    return len(number)

sum = 0
for i in range(1, 1001):
    sum += char_num(i)

print(sum)
