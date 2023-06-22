# Starting with linear search

def linear_search(x, arr):
    for index, value in enumerate(arr):
        if value == x:
            return index

    return -1


arr = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]





print(linear_search(8, arr))





















