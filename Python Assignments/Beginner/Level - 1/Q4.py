#Q4

def odd_sum(n1, n2):
    total = 0
    for i in range(n1, n2 + 1):
        if i % 2 == 1:
            total += i
    return total
    
print(odd_sum(1, 10))