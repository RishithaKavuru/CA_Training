#Q11

def sum_of_digits(n):
    while n >= 10:
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        n = digit_sum
    return n

num = int(input("num = "))
final_sum = sum_of_digits(num)
print("Sum_of_digits =", final_sum)