def selection_sort(arr):
    """
    Selection sort algorithm.
    Args:
        arr: list of integers
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    arr = [1, 4, 3, 2, 5]
    print(selection_sort(arr))
