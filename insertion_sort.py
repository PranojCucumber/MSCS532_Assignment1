def insertion_sort_decreasing(arr):
    """
    Sorts an array in monotonically decreasing order using the Insertion Sort algorithm.

    Parameters:
    arr (list): A list of elements to be sorted.

    Returns:
    None: The list is sorted in place.
    """
    # Loop through each element in the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be compared
        j = i - 1     # The index of the last sorted element

        # Move elements that are less than key to one position ahead of their current position
        while j >= 0 and key > arr[j]:  # Change '<' to '>' for decreasing order
            arr[j + 1] = arr[j]  # Shift the larger element to the right
            j -= 1  # Move to the next element on the left

        arr[j + 1] = key  # Place the key in its correct position

# Example usage of the function
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]  # Example array
    print("Original array:", data)
    insertion_sort_decreasing(data)  # Sort the array
    print("Sorted array in decreasing order:", data)  # Print the sorted array
