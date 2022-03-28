
def insertion_sort(arr):
    """
    Insertion sort algorithm.
    Args:
        arr: list of integers
    """
    for i in range(1, len(arr)):
        current = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > current:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = current
                break
            if j == 0:
                arr[j] = current


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    insertion_sort(arr)
    print(arr)
