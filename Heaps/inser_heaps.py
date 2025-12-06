def heapify(arr, n, i):
    parent = int((i-1)/2)

    if parent >= 0:
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent]