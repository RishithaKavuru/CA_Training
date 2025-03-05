#Q6

def power_of_two(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    return power_of_two(n // 2)
    
n = int(input())
print(power_of_two(n))