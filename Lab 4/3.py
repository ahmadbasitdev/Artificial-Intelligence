"""Lab 4 - Task 3: Implement binary search."""


def binary_search(arr: list[int], target: int) -> int:
    """Return the index of target in a sorted list, or -1 if not found."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1 

    return -1 


def main() -> None:
    """Read a target value and search the sample sorted list."""
    print("=== Lab 4 - Task 3: Binary Search ===")
    values = [6, 12, 17, 23, 38, 45, 77, 84, 90]
    try:
        target = int(input("Enter the number you want to search: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    result = binary_search(values, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found.")


if __name__ == "__main__":
    main()