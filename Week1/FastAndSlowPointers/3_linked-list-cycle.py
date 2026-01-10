### Problem: Linked List Cycle

'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false

'''

import pytest

class ListNodes:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

# Helper function to create linked lists with optional cycles for testing
def create_linked_list_with_cycle(nodes_val, pos):
    if not nodes_val:
        return None

    nodes = [ListNodes(val) for val in nodes_val]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        # Create the cycle: the last node points to the node at index 'pos'
        nodes[-1].next = nodes[pos]

    return nodes[0]

###############################################################
def has_cycle(head: ListNodes) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

###############################################################
# --- Test Cases using pytest ---

@pytest.mark.parametrize("values, pos, expected", [
    ([3, 2, 0, -4], 1, True),   # Standard cycle
    ([1, 2], 0, True),          # Two-node cycle
    ([1], -1, False),           # Single node, no cycle
    ([1], 0, True),             # Single node, points to itself
    ([1, 2, 3], -1, False),     # No cycle
    ([], -1, False),            # Empty list
])

def test_has_cycle(values, pos, expected):
    head = create_linked_list_with_cycle(values, pos)
    assert has_cycle(head) == expected

# --- Execution Block ---
if __name__ == "__main__":
    # Use -v for verbose output and -p no:warnings to keep it clean
    pytest.main([__file__, "-v", "-p", "no:warnings"])


