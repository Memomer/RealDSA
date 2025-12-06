def heapify(arr, n, 1):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if (l < n and arr[l] > arr[largest]):
        largest = l

    if (r < n and arr[r] > arr[largest]):
        largest = r
    
    if (largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

    
def deleteRoot(arr):
    global n

    lastElement = arr[n - 1]
    arr[0] = lastElement
    n = n - 1
    heapify(arr, n, 0)

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':

    arr = [10, 5, 3, 2, 4]

    n = len(arr)

    deleteRoot(arr)

    printArray(arr, n)