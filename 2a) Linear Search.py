def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
key = 30
print("Found at index:", linear_search(arr, key))
