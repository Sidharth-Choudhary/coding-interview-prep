### Problem: Linked List Cycle III

'''
Statement
Given the head of a linked list, determine the length of the cycle present in the linked list. If there is no cycle, return 0.

A cycle exists in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Constraints:
    1) The number of nodes in the list is in the range [0,10^4].
    2) −10^5≤ Node.value ≤ 10^5
'''

import pytest

class ListNodes:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next


# --- Helper Function to Build the List with Cycle ---
def build_cycle_list(values, pos):
    if not values:
        return None

    nodes = [ListNodes(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]
        return nodes[0], nodes[pos]  # Return head and expected start node

    return nodes[0], None  # Return head and None for no cycle

###############################################################

def count_cycle_length(head):
    ## Write your code here
    return

###############################################################

@pytest.mark.parametrize("values, pos, expected_length", [
    ([3, 2, 0, -4], 1, 3),    # Cycle: 2 -> 0 -> -4 -> (back to 2) Length 3
    ([1, 2], 0, 2),           # Cycle: 1 -> 2 -> (back to 1) Length 2
    ([1, 2, 3, 4, 5], -1, 0), # No cycle, Length 0
    ([1], 0, 1),              # Single node cycle, Length 1
])
def test_count_cycle_length(values, pos, expected_length):
    head, _ = build_cycle_list(values, pos)
    assert count_cycle_length(head) == expected_length

# --- Execution Block ---
if __name__ == "__main__":
    # Use -v for verbose output and -p no:warnings to keep it clean
    pytest.main([__file__, "-v", "-p", "no:warnings"])
