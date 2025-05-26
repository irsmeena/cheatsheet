# Import the Lab3 module where the bubble_sort function is defined
import Lab3

# Print a header to indicate the test script is running
print("Test_Lab3")


# ✅ Test Case 1: Check sorting in ascending order
def test_bubble_sort_ascending():
    result = []  # Variable to hold the sorting result
    input_arr = [64, 34, 25, 12, 22, 11, 90, 95, 105, 110]  # Unsorted input
    test_arr = [11, 12, 22, 25, 34, 64, 90, 95, 105, 110]   # Expected sorted output


             #Lab3.SORT_ASCENDING is called through import Lab3
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)  # Call bubble_sort with ascending order

    assert (result == test_arr)  # Assert that the output matches expected


# ✅ Test Case 2: Check sorting in descending order
def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 95, 105, 110]
    test_arr = [110, 105, 95, 90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)


# ✅ Test Case 3: Invalid sorting order provided
def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)  # 3 is an invalid sorting order

    assert (result == [])  # Should return an empty list


# ✅ Test Case 4: List has more than 10 elements (REQ-03)
def test_bubble_sort_more_than_10():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 88, 75, 43, 23]  # 11 elements

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)  # Should return 1 when list has more than 10 items


# ✅ Test Case 5: Valid short list (5 elements), test ascending order
def test_bubble_sort_less():
    result = []
    input_arr = [64, 34, 25, 12, 22]
    test_arr = [12, 22, 25, 34, 64]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(result == test_arr)


# ✅ Test Case 6: List contains a non-integer (REQ-05)
def test_bubble_check_int():
    result = []
    input_arr = [45, 10, 20, 15, "dog", 6, 7]  # Contains a string "dog"

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(result == 2)  # Should return 2 for invalid data type


# ✅ Test Case 7: Empty list (REQ-04)
def test_bubble_sort_empty():
    result = []
    input_arr = []  # Empty list

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert(result == 0)  # Should return 0 for empty list
