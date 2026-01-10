'''
Docstring for Algorithm.Week1.TwoPointers.3_sort-colors

Problem: Sort Colors
Statement
Given an array, colors, which contains a combination of the following three elements:

0 (Representing red)

1 (Representing white)

2 (Representing blue)

Sort the array in place so that the elements of the same color are adjacent, and the final order is: red (0), then white (1), and then blue (2).

Note: You are not allowed to use any built-in sorting functions. The goal is to solve this efficiently without extra space.
'''
import pytest

def sortColors(colors):
    low, mid, high = 0, 0, len(colors) - 1

    while mid <= high:
        if colors[mid] == 0:
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1
        elif colors[mid] == 1:
            mid += 1
        else:
            colors[mid], colors[high] = colors[high], colors[mid]
            high -= 1

    return colors


# --- Pytest Parametrized Tests ---

@pytest.mark.parametrize("input_list, expected", [
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]), # Standard case
    ([0, 1, 2], [0, 1, 2]),                   # Already sorted
    ([2, 0, 1], [0, 1, 2]),                   # All three colors, mixed
    ([1, 1, 0, 0], [0, 0, 1, 1]),             # Only two colors (0 and 1)
    ([2, 2, 2], [2, 2, 2]),                   # Single color only
    ([], []),                                 # Empty list edge case
])

def test_sortColors(input_list, expected):
    # Copy the list to avoid modifying the input parametrization data
    case = input_list[:]
    sortColors(case)
    assert case == expected

# --- Run with 'python func.py' ---
if __name__ == "__main__":
    pytest.main([__file__, "-v", "-p", "no:warnings"])


