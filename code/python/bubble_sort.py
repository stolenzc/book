
def bubble_sort(arr):
    """
    Bubble sort algorithm.
    Args:
        arr: list of integers
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    print(bubble_sort(arr))
