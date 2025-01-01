"""
Combinations of an array of integers

------------------------------------------------
Understand combinations of an array of integers.
------------------------------------------------

Combinations of an array of integers are the number of ways to choose k elements from an array of n elements.
For example, if we have an array [1, 2, 3] and we want to choose any 2 elements from it without considering the order, the combinations are:

[1, 2], [1, 3], [2, 3]

So there are 3 combinations.

So what is the focus here?

We need to find the number of ways (combinations) to choose k elements from an array of n elements. and also
We need to find the combinations of an array of integers itself. 
"""

# Solution 1: Simple yet efficient implementation using recursion but it does not allow duplicates
# Time Complexity: O(n^k)
# Space Complexity: O(k)
def combinations_of_an_array(
        array: list[int],
        k: int
    ) -> list[list[int]]:
    """
    Pseudocode to visualise the solution:
    
    1. Initialize an empty set to check if the current combination is already seen.
    2. Initialize an empty list to store the possible final combinations.
    3. Since we are using recursion, we need to define a helper function that actually does the work.
    
    Understanding the flow here is important. Try to visualise the flow of the code. 
    Or just use examples and print statements to see the flow.

    This is just a visualisation of the flow of the code for the array [1, 2, 3] and k = 2

    Step 1: []                  # Start with empty
    Step 2: [1]                 # Add 1
    Step 3: [1,2]               # Found valid combination
    Step 4: [1]                 # Remove 2 (backtrack)
    Step 5: [1,3]               # Found valid combination
    Step 6: [1]                 # Remove 3 (backtrack)
    Step 7: []                  # Remove 1 (backtrack)
    Step 8: [2]                 # Add 2
    Step 9: [2,3]               # Found valid combination
    Step 10: []                 # Backtrack to empty
    """

    seen = set()
    combinations = []

    def backtrack(
            start: int, 
            current_combo: list[int]
        ) -> None:
        # Base case: if current combination has k elements, add it to results
        # Because that's what we want, we want k elements in each combination
        if len(current_combo) == k:
            # Convert the current_combo to a tuple and add it to the seen set
            # This is to check if the current combination is already seen
            non_duplicate_combo = tuple(current_combo)
            if non_duplicate_combo not in seen:
                seen.add(non_duplicate_combo)
                combinations.append(current_combo[:])
            return
            
        # Try adding each remaining element to the current combination
        for i in range(start, len(array)):
            current_combo.append(array[i])
            backtrack(i + 1, current_combo)
            current_combo.pop()  
    
    # We have to call the backtrack function with the initial parameters,
    # Start = 0 and current_combo = []
    backtrack(0, [])

    return combinations