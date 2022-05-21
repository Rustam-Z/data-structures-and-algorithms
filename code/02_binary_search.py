def binary_search(self, nums, target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return -1


# Returns index of x in arr if present, else -1
def binary_search_recursive(arr, l, r, x):
    # Check base case
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binary_search_recursive(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binary_search_recursive(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
