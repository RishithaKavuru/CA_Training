#Q7

def median(number_list):
    number_list.sort()
    n = len(number_list)
    mid = n // 2
    
    if n % 2 == 0:
        return (number_list[mid - 1] + number_list[mid]) / 2
    else:
        return number_list[mid]

number_list = [7, 2, 5, 1, 9, 3]
print("Median:", median(number_list))