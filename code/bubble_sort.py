"""
Optimized Bubble sort algorithm implementation.
Time Complexity: O(n^2)
    Best O(n)
    Worst O(n^2)
    Average O(n^2)
Space Complexity: O(1)
"""


def bubble_sort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break

    return array


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9, 32, 43, 0, 92]
    bubble_sort(data)
    print(data)
