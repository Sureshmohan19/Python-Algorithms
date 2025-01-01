"""
Find all permutations of an array.

Understand the problem:

Given an array of integers, find all permutations of the array and sort them in ascending order.
I will also use itertools.permutations to find all permutations of the array at the end to check if my solution is correct,
and to make things easier in real life.

"""
from typing import Union

# Time Complexity: O(n * n!)
# Space Complexity: O(n)
def find_all_permutations(
        array: list[Union[int, float]]
) -> list[Union[int, float]]:
    """
    Find all permutations of an array
    
    Workflow:
    
    1. We already discussed how to find combinations of an array in the previous problems. Look for combinations.py for more details.
    2. So here, we are doing almost the same thing but instead of combinations, we are finding permutations.

    3.1 We will use backtracking to find all permutations.
    3.2 We have to use a helper function to do the backtracking and call this function initially with start = 0.
    
    I think its best to explain the backtracking process with an example from here.

    ------------------------------------------------------------------------------------------------
    Take an example of array = [1, 2, 3] which has length of 3 and 6 permutations.

    array = [1,2,3]

    # LEVEL 1: start = 0
    # -----------------------------
    # Current array: [1,2,3]
    # i = 0 (first iteration)
    # - Swap array[0] and array[0]: 1↔1
    # Result: [1,2,3] (no change)
    # Call backtrack(1)

        # LEVEL 2: start = 1
        # -----------------------------
        # First iteration (i = 1):
        # - Swap array[1] and array[1]: 2↔2
        # Result: [1,2,3]
        # Call backtrack(2)
        
            # LEVEL 3: start = 2
            # -----------------------------
            # We're at last position!
            # Save first permutation: [1,2,3]
            # Return to Level 2
        
        # Still at LEVEL 2
        # Second iteration (i = 2):
        # - Swap array[1] and array[2]: 2↔3
        # Result: [1,3,2]
        # Call backtrack(2)
        
            # LEVEL 3: start = 2
            # -----------------------------
            # We're at last position!
            # Save second permutation: [1,3,2]
            # Return to Level 2
        
        # Back at LEVEL 2
        # Swap back array[1] and array[2]: 3↔2
        # Result: [1,2,3]

    # Current array: [1,2,3]
    # i = 1 (second iteration)
    # - Swap array[0] and array[1]: 1↔2
    # Result: [2,1,3]
    # Call backtrack(1)

        # LEVEL 2: start = 1
        # -----------------------------
        # First iteration (i = 1):
        # - Swap array[1] and array[1]: 1↔1
        # Result: [2,1,3]
        # Call backtrack(2)
        
            # LEVEL 3: start = 2
            # -----------------------------
            # We're at last position!
            # Save third permutation: [2,1,3]
            # Return to Level 2
        
        # Still at LEVEL 2
        # Second iteration (i = 2):
        # - Swap array[1] and array[2]: 1↔3
        # Result: [2,3,1]
        # Call backtrack(2)
        
            # LEVEL 3: start = 2
            # -----------------------------
            # We're at last position!
            # Save fourth permutation: [2,3,1]
            # Return to Level 2
        
        # Back at LEVEL 2
        # Swap back array[1] and array[2]: 3↔1
        # Result: [2,1,3]
    ------------------------------------------------------------------------------------------------

    """

    output_list = []

    def backtrack(start: int) -> None:
        # When we reach the end of the array, we add the current permutation to the output list
        if start == len(array) - 1:
            output_list.append(array[:])
            return
        
        # Try each element in current position
        for i in range(start, len(array)):
            # Swap the current element with the element at the current position
            array[start], array[i] = array[i], array[start]
            # Recurse on the next position
            backtrack(start + 1)
            # Backtrack by swapping the current element with the element at the current position
            array[start], array[i] = array[i], array[start]

    # Start the backtracking process from the first element
    backtrack(start=0)
    return output_list


# Practical Implementation
from itertools import permutations

def permute(nums: list[int]) -> list[list[int]]:
    return list(permutations(nums))


