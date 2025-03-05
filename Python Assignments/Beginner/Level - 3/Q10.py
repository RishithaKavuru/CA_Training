#Q10

def customers_left(N, S):
    arrived = set()  
    occupied = set() 
    left_customers = 0

    for customer in S:
        if customer in arrived:
            if customer in occupied:  
                occupied.remove(customer)  
        else:
            arrived.add(customer)
            if len(occupied) < N:
                occupied.add(customer) 
            else:
                left_customers += 1 

    return left_customers
