"""
Heap sort algorithm implementation.
Time complexity: best, worst, average = O(n log n)
Space complexity: O(1)
"""


def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # heapify root element
        heapify(arr, i, 0)


if __name__ == "__main__":
    unsorted_array = [12, 11, 13, 5, 6, 7]
    heap_sort(unsorted_array)
    print(unsorted_array)
