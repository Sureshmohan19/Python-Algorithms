"""
Tuples/Lists to flattened list
"""

from typing import Union

# Solution 1: Simple way to convert tuples and lists to list
# Time Complexity: O(n)
# Space Complexity: O(d) where d is the depth of the nested tuples/lists
def tuples_to_list(
        data: Union[tuple, list],
        output_type: Union[list, tuple] = list
) -> Union[list, tuple]:
    """
    Pseudocode to visualise the solution:
    
    1. When we call this function, we pass the tuples or list as an argument. 
        1.1 input constraints are, that either it can be a single whole tuples or a nested tuples. 
        1.2 For example, if the input is (1, (2, 3), (4, (5, 6))) then the output should be [1, 2, 3, 4, 5, 6]
    2. The call to this function will directly call the return statement first since we are calling helper function inside it.

    ------------------------------------------------------------------------------------------------
    ** Helper function to flatten the list **

    3.1 This function will accept the tuples or list as an argument (our input)
    3.2 It will then iterate over the inputs and check if each element is either a tuple/list or just an individual element.
    3.3 If its a tuple/list, it will call the helper function again with the element as an argument.
    3.4 If its an individual element, it will yield the element.
    3.5 This will continue until we have iterated over the entire input.
    3.6 We will return the final list.

    ** End of helper function **
    ------------------------------------------------------------------------------------------------

    Understanding the flow of the code:
    data = (1, (2, 3), (4, (5, 6)))

    # Flow:
    1. flatten_list(data)
    → sees 1: yields 1
    → sees (2,3): yield from flatten_list((2,3))
        → yields 2
        → yields 3
    → sees (4,(5,6)): yield from flatten_list((4,(5,6)))
        → yields 4
        → sees (5,6): yield from flatten_list((5,6))
            → yields 5
            → yields 6

    # Final result: 1,2,3,4,5,6 (one at a time)

    """

    def flatten_list(sequence: Union[tuple, list]):
        for item in sequence:
            if isinstance(item, (tuple, list)):
                yield from flatten_list(item)
            else:
                yield item

    # This is the final list that we are returning
    return output_type(flatten_list(data))
