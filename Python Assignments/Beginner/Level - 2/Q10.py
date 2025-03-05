#Q10

def stone_piles(n):
    piles = []
    
    if n % 2 == 0:
        start = 2
    else:
        start = 1
        
    while start < n:
        piles.append(start)
        start += 2
    return piles
    
n = int(input("n: "))
print("Stones in a single pile",(stone_piles(n)))