#Q1

def find_common_elements(l1, l2):
    common_elements = []
    for element in l1:
        if element in l2:
            common_elements.append(element)
    return common_elements

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

print(find_common_elements(l1, l2))