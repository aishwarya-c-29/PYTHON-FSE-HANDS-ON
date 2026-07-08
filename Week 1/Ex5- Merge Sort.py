# Merge Sort

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        # Divide
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge two halves
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # Remaining elements of left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Remaining elements of right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# User Input
n = int(input("Enter number of elements: "))

arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

print("Before sorting:", arr)
merge_sort(arr)
print("After sorting:", arr)

"""
Output:
Enter number of elements: 6
Enter elements:
45
12
8
30
25
10
Before sorting: [45, 12, 8, 30, 25, 10]
After sorting: [8, 10, 12, 25, 30, 45]
