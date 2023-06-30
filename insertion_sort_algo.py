# Insertion sort Algo works the same way bubble Sort the only difference is the time complexities thus rendering insertion better

def insertion_sort(arr):
    n = len(arr)

    # An outer for loop to go through the list

    for i in range(n):
        key = arr[i]  # element to go through sorting
        j = i - 1  # represents the index of the before element

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

            arr[j] = key

    return arr


arr = [1, 3, 4, 5, 50, 8, 20, 40, 70, 45, 68, 90, 20]

insertion_sort(arr)

print(arr)
