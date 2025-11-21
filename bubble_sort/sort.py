def bubble_sort(arr):
    """
    Sorts an array using bubble sort algorithm.

    Args:
        arr (list): List of comparable elements

    Returns:
        list: New sorted list
    """
    n = len(arr)
    output = arr.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if output[j] > output[j+1]:
                output[j], output[j+1] = output[j+1], output[j]
    return output

if __name__ == "__main__":
    demo = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", demo)
    print("Sorted array:", bubble_sort(demo))