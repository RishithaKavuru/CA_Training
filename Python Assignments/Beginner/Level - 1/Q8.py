#Q8

import math

def lcm(n1, n2):
    return abs(n1 * n2) // math.gcd(n1, n2)

n1 = int(input())
n2 = int(input())
print(f"LCM of {n1} and {n2} are: {lcm(n1, n2)}")