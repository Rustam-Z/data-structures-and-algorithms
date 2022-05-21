"""
Insertion sort algorithm implementation.
Time complexity:
    Best O(n)
    Worst O(n^2)
    Average O(n^2)
Space complexity: O(1)
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


if __name__ == '__main__':
    unsorted_array = [5, 2, 4, 6, 1, 3]
    sorted_array = insertion_sort(unsorted_array)
    print(sorted_array)
