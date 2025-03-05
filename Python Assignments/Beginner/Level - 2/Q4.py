#Q4

def rotate_array(arr, D):
    return arr[-D:] + arr[:-D]

arr = [1, 2, 3, 4, 5]
D = 2

print("arr after rotation:", rotate_array(arr, D))