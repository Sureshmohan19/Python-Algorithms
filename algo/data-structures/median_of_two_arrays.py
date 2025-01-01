"""
Find the median of two arrays

--------------------------------
Understand the problem:
--------------------------------

Given two sorted arrays of integers, find the median of the two arrays. 
This simple implementation is just for the purpose of learning. 
In reality, we will use binary search to find the median which is more time efficient.

"""

def find_median_of_two_arrays(
        array1: list[int],
        array2: list[int]
) -> float:
    """
    Find the median of two arrays

    Workflow:
    1. Merge the two arrays using list concatenation (array1 + array2)
    2. Sort the merged array
    3.1 If the length of the merged array is odd, return the middle element
    3.2 If the length of the merged array is even, return the average of the two middle elements

    ------------------------------------------------------------------------------------------------
    Why n-1 and n instead of n and n+1?
    ------------------------------------------------------------------------------------------------

    If the length of the merged array is even, the two middle elements are the median

    First middle: (n/2) - 1
    Second middle: n/2
    Since array indices start at 0, we need to subtract 1 to get the first middle element
    The second middle element is already at the correct position because integer division rounds down

    ------------------------------------------------------------------------------------------------
    Read this only if you are confused still:
    ------------------------------------------------------------------------------------------------

    For example, lets consider an array [1,2,3,4] with length 4. Median should be 2.5.

    ------------------------------------------------------------------------------------------------
    With 0-based indexing:
    array: [1,2,3,4]
    its' index: [0,1,2,3]

    The first part is, total_elements // 2 = 4 // 2 = 2 (this is the index of the first middle element) which is 3 in 0-based indexing
    The second part is, total_elements // 2 - 1 = 4 // 2 - 1 = 1 (this is the index of the second middle element) which is 2 in 0-based indexing

    So, the first middle element is at index 3 and the second middle element is at index 2.
    The median is the average of the two middle elements: (3 + 2) / 2 = 2.5

    ------------------------------------------------------------------------------------------------
    With 1-based indexing:
    array: [1,2,3,4]
    its' index: [1,2,3,4]

    The first part is, total_elements // 2 = 4 // 2 = 2 (this is the index of the first middle element) which is 2 in 0-based indexing
    The second part is, total_elements // 2 + 1 = 4 // 2 + 1 = 3 (this is the index of the second middle element) which is 3 in 0-based indexing

    So, the first middle element is at index 2 and the second middle element is at index 3.
    The median is the average of the two middle elements: (2 + 3) / 2 = 2.5

    ------------------------------------------------------------------------------------------------

    """

    merged_arrays = sorted(array1 + array2)
    total_elements = len(merged_arrays)

    # IF odd, return the middle element
    if total_elements % 2 == 1:
        return float(merged_arrays[total_elements // 2])
    
    elif total_elements % 2 == 0:
        # IF even, return the average of the two middle elements
        return float((merged_arrays[total_elements // 2 - 1] + merged_arrays[total_elements // 2]) / 2.0)

    else:
        raise ValueError("Invalid array length")
