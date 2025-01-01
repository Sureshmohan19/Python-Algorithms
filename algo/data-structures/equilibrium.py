"""
Finding Equilibrium index of an array

--------------------------------
Understand equilibrium index.
--------------------------------

Imagine an array of ints and think an index i where the sum of elements to its left is equal to its right. 
If such an index exists, it is called an equilibrium index.

If is none, return -1 for the index to understand that there is no equilibrium index.
"""

# Solution 1: Not at all efficient but simple to understand
# Time Complexity: O(n^2)
def equilibrium_index_of_an_array_inefficient(array: list[int]) -> int:
    
    """
    Pseudocode to visualise the solution:
    
    1. Then iterate over the array and for each element, calculate the sum of elements to its left and right.
    2. If the sum of elements to its left is equal to its right, return the index.
    3. If no such index is found, return -1.
    
    Simple to understand but not efficient since we need to iterate over the array twice to calculate the sum of elements to its left and right.
    """

    for i in range(len(array)):
        if sum(array[:i]) == sum(array[i+1:]):
            return i
    return -1

# Solution 2: Efficient way to implement this problem
# Time Complexity: O(n)
# Space Complexity: O(1)
def equilibrium_index_of_an_array_efficient(array: list[int]) -> int:
    """
    Psuedocode to visualise the solution
    
    1. First calculate the sum of total integers in an array - only once
    2. Then take a variable to store the sum of elements to its left and initialize it to 0 (because at start, there are no elements to its left)
    3. Then iterate over the array and for each element, calculate the sum of the elements to its right. 
      3.1. The real question is how? 
      3.2. Simple -> take total sum - left sum (the variable we initialized) - current element (the element we are iterating over)
    4. If the sum of elements to its right is equal to the sum of elements to its left, return the index.
    5. IF or IF NOT, update the left sum by adding the current element to it, because we are moving to the next element so left_sum variable should be updated.
    6. If no such index is found, return -1 for the index to understand that there is no equilibrium index.

    This is efficient because we are iterating over the array only once and calculating the sum of elements to its right in O(1) time,
    and also space complexity is O(1) since we are not using any extra space that grows with the input size.
    """

    total_sum = sum(array)
    left_sum = 0

    for i in range (len(array)):
        right_sum =  total_sum - left_sum - array[i]
        if left_sum == right_sum:
            return i
        left_sum += array[i]
    return -1