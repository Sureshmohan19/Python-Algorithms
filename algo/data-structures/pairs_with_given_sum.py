"""
Find pairs with given sum in an array. 

Understand the problem:

Given an array of integers, # of combinations and a target sum, 
find all pairs of integers in the array that add up to the target sum.

"""
from typing import Union, Tuple
from itertools import combinations

def find_pairs_with_given_sum(
        array: list[Union[int, float]],
        num_combinations: int,
        target_sum: int,
        combinations_output: bool = False
) -> Union[list[Tuple[Union[int, float], ...]], int]:
    """
    Find pairs with given sum in an array

    Workflow:
    1. We already discussed how to find combinations of an array in the previous problems. Look for combinations.py for more details.
    2. So here, we just use itertools.combinations to find all combinations of the array to make things easier.
    3. Once we get combinations, we can use a simple loop to check if the sum of any combination is equal to the target sum.
    4. If it is, we add it to the result list as a tuple and also increment the count of combinations.
    5. If the combinations_output is True, we return the result list.
    6. If the combinations_output is False, we return the count of combinations only.

    """

    # Initialize the output list and count of combinations
    output_list = []
    count = 0

    # Check if the sum of any combination is equal to the target sum by iterating through all combinations
    for combination in combinations(array, num_combinations):
        if sum(combination) == target_sum:
                output_list.append(combination)
                count += 1

    # Return only the count of combinations if combinations_output is False
    return count if not combinations_output else (count, output_list)
