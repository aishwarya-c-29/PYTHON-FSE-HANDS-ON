# Binary Search 

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif target > arr[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# User input
n = int(input("Enter number of elements: "))

arr = []

print("Enter elements in sorted order:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter element to search: "))


# Function call
result = binary_search(arr, target)


# Display result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

"""
Output:
Enter number of elements: 5
Enter elements in sorted order:
10
20
30
40
50
Enter element to search: 40
Element found at index: 3
"""
