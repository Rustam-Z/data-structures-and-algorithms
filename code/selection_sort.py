"""
Selection sort algorithm implementation.
Time Complexity:
    Best O(n^2)
    Worst O(n^2)
    Average O(n^2)
Space Complexity: O(1)
"""


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    unsorted_array = [5, 3, 6, 2, 10, -23, 0]
    selected_array = selection_sort(unsorted_array)
    print(selected_array)
