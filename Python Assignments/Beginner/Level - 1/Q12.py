#Q12

def reverse_number(n):
    revnum = 0
    while n > 0:
        revnum = revnum * 10 + n % 10
        n //= 10
    return revnum

num = int(input("num = "))
reversed_num = reverse_number(num)
print("revnum =", reversed_num)
