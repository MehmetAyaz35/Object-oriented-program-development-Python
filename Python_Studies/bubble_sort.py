def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1, swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
                
# for i in range(5):   #0,1,2,3,4
#     print(i)