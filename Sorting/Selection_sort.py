def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    print(arr)

# Main
arr = [64, 25, 12, 22, 11]
selection_sort(arr)