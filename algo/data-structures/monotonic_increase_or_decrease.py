"""
Given an array of integers, determine whether the array is monotonic increasing or decreasing


-------------------------------
Understand the problem:
-------------------------------
1. We need to determine whether the array is monotonic increasing or decreasing
2. Monotonic increasing means that each element is greater than or equal to the previous element
3. Monotonic decreasing means that each element is less than or equal to the previous element

"""

from typing import Union, Literal

# Time Complexity: O(n)
# Space Complexity: O(1)
def is_monotonic(
        array: list[Union[int|float]],
        type: Literal["increasing", "decreasing"]
) -> bool:
    """
    Determine whether the array is monotonic increasing or decreasing

    Workflow:
    1. Iterate through the array
    2. For monotonic increasing, 
        2.1 Check if the current element is greater than or equal to the previous element
        2.2 If not, return False
    3. For monotonic decreasing, 
        3.1 Check if the current element is less than or equal to the previous element
        3.2 If not, return False
    """

    if len(array) <= 1:
        return True

    if type == "increasing":
        """
        Alternatively, we can use the following approach:
        return all(array[i] >= array[i-1] for i in range(1, len(array)))
        """
        for i in range (1, len(array)): 
            if array[i] <= array[i-1]:
                return False
        return True       
            
    elif type == "decreasing":
        """
        Alternatively, we can use the following approach:
        return all(array[i] <= array[i-1] for i in range(1, len(array)))
        """
        for i in range (1, len(array)): 
            if array[i] >= array[i-1]:
                return False
        return True        
    
    else:
        raise ValueError("Invalid type")
