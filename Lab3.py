# Print the title of the lab
print("Lab 3 - Software Unit Testing with PyTest")

# Constants for sorting order
SORT_ASCENDING = 0        # Represents sorting in ascending order
SORT_DESCENDING = 1       # Represents sorting in descending order

# Function to perform bubble sort
def bubble_sort(arr, sorting_order):
    # REQ-05: Check if all elements in the array are integers
    for s in arr: 
        if type(s) is not int:      # If any element is not an integer
            return 2                # Return 2 to indicate invalid input

    # Copy the input list to avoid changing the original
    arr_result = arr.copy()

    # Get the number of elements in the array
    n = len(arr_result)
    print("Number of elements in the list: ", n)

    # REQ-04: If list is empty, return 0
    if n == 0:
        return 0

    # REQ-03: If list has more than 10 elements, return 1
    elif n > 10:
        arr_result = 1  # Not performing sorting, just returning 1 as a flag

    else:
        # Only proceed with sorting if list length is 10 or less

        # Outer loop to go through each element (n-1 times)
        for i in range(n - 1):
            # Inner loop for comparing adjacent elements
            for j in range(0, n - i - 1):

                #REQ-01

                # If sorting in ascending order
                if sorting_order == SORT_ASCENDING:
                    # Swap if elements are out of order
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                #REQ-02

                # If sorting in descending order
                elif sorting_order == SORT_DESCENDING:
                    # Swap if elements are out of order
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Invalid sorting order: return an empty list
                    arr_result = []

    # Return the final sorted array or error code (0, 1, 2)
    return arr_result

# Main function to run the program
def main():
    # Create an empty list to sort
    arr = []

    # Try to sort the list in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Try to sort the same list in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

# Execute the main function if this file is run as a script
if __name__ == "__main__":
    main()
