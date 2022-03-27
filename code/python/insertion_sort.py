
def insertion_sort(arr):
    """
    Insertion sort algorithm.
    Args:
        arr: list of integers
    """
    for i in range(1, len(arr)):
        for j in range(i-1, 0, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    insertion_sort(arr)
    print(arr)
