#Q6

def is_perfect_number(n):
    if n < 1:
        return("No")
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n

n = int(input())
if is_perfect_number(n):
    print("Yes")
else:
    print("No")