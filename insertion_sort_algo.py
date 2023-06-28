# Insertion sort Algo works the same way like bubble Sort the only difference is the time complexities thus rendering insertion better

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key_value = arr[i]  # Represents the value to be sorted
        last_elem = i - 1

        while last_elem >= 0 and arr[last_elem] > key_value:
            arr[last_elem + 1]  = arr[last_elem]
            last_elem -= 1

            arr[last_elem + 1] = key_value  # Sorting it into the list i respect to its value

    return arr


arr = [1, 3, 4, 5, 1, 50, 30, 40, 80, 70, 90]

insertion_sort(arr)

print(arr)
