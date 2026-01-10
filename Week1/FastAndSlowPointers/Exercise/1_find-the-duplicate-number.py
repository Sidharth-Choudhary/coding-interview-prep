### Problem: Find The Duplicate Number
'''
Given an array of positive numbers, nums, such that the values lie in the range [1,n] inclusive, and that there are n+1 numbers in the array,
find and return the duplicate number present in nums. There is only one repeated number in nums, but it may appear more than once in the array

Input -- nums = [6,6,6,4,6,6,6]
Output -- 6

Input -- nums = [1,2,3,4,5,6,6,7]
Output -- 6
'''

import pytest

def find_duplicates(nums):
    ## Write your code here
    return



# --- Pytest Parametrized Tests ---

@pytest.mark.parametrize("nums, expected", [
    ([1, 3, 4, 2, 2], 2),       # Duplicate is 2
    ([3, 1, 3, 4, 2], 3),       # Duplicate is 3
    ([1, 1], 1),                # Smallest array
    ([1, 1, 2], 1),             # Duplicate at the start
    ([2, 2, 2, 2, 2], 2),       # All elements are duplicates
    ([2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9), # Larger array
])

def test_find_duplicate(nums, expected):
    assert find_duplicates(nums) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-p", "no:warnings"])