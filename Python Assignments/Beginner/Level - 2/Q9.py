#Q9

numbers = [1, 2, 3, 4, 5]

try:
    index = int(input())
    print("Element at index:", numbers[index])
except IndexError:
    print("Index out of range")
