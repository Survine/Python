def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

arr = [5,9,4,1,2,7,3,8]
target = 7

if linear_search(arr, target):
    print("Element found")
else:
    print("Element not found")