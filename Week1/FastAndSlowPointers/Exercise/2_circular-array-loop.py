### Problem: Circular Array Loop

'''
Statement
There is a circular list of non-zero integers called nums. Each number in the list tells you how many steps to move forward or backward from your current position:
If nums[i] is positive, move nums[i] steps forward.
If nums[i] is negative, move nums[i] steps backward.
As the list is circular:
Moving forward from the last element takes you back to the first element.
Moving backward from the first element takes you to the last element.
A cycle in this list means:
You keep moving according to the numbers, and you end up repeating a sequence of indexes.
All numbers in the cycle have the same sign (either all positive or all negative).
The cycle length is greater than 1 (it involves at least two indexes).
Return true if such a cycle exists in the list or false otherwise.

Example
nums = [3,1,2]
o/p: True
nums = [-2,-1,-3]
o/p: True
nums = [2,1,-1,-2]
o/p: False
nums = [3,-3,1,1]
o/p: True
'''

import pytest


def circularArrayLoop(nums):

    ## Write your code here

    return

# --- Pytest Parametrized Tests ---

@pytest.mark.parametrize("nums, expected", [
    ([2, -1, 1, 2, 2], True),   # Forward cycle: 0 -> 2 -> 3 -> 0
    ([-1, 2], False),           # Mixed directions: -1 is backward, 2 is forward
    ([2, 4, 1, 1, 1], True),    # Long forward cycle
    ([-2, 1, -1, -2], False),   # Single-node loop (index 1 to index 1)
    ([1, 2, 3, 4, 5], True),    # Large wrap-around cycle
    ([3, 1, 2], True),          # Cycle: 0 -> (0+3)%3 = 0 (Length 1, should be False)
    ([-1, -2, -3, -4, -5], False), # Entirely backward cycle
    ([-1, -1, -1, -1, -1], True) # Entirely backward cycle
])

def test_circularArrayLoop(nums, expected):
    # We pass the input to the function and check if result matches expected
    assert circularArrayLoop(nums) == expected

# --- Execution Block ---
if __name__ == "__main__":
    # Use -v for verbose output and -p no:warnings to keep it clean
    pytest.main([__file__, "-v", "-p", "no:warnings"])

