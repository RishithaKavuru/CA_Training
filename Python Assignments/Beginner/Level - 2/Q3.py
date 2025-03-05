#Q3

def count_pairs(arr, k):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                count += 1
    return count

arr = [1, 2, 3, 4, 5]
k = 6

print("Pair count:", count_pairs(arr, k))
