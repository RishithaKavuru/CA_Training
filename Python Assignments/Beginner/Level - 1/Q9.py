#Q9

def frequency(input_list):
    frequency_count = {}
    for num in input_list:
        if num in frequency_count:
            frequency_count[num] += 1 
        else:
            frequency_count[num] = 1 
    return frequency_count

input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
print(frequency(input_list))