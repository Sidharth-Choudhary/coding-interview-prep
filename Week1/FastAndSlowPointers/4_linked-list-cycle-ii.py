### Problem: Linked List Cycle II

'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

'''

import pytest

class ListNodes:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

# Helper function to create linked lists with optional cycles for testing
def create_linked_list_with_cycle(nodes_val, pos):
    if not nodes_val:
        return None, None

    nodes = [ListNodes(val) for val in nodes_val]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    cycle_entry_node = None
    if pos != -1:
        # Create the cycle: the last node points to the node at index 'pos'
        nodes[-1].next = nodes[pos]
        cycle_entry_node = nodes[pos]
    return nodes[0],cycle_entry_node

###############################################################

def detect_cycle(head: ListNodes):

    slow = head
    fast = head

    ##  find the intersection
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            ## Find the entrance
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

###############################################################

## --- Parametrized Test Suite ---

@pytest.mark.parametrize("values, pos", [
    ([3, 2, 0, -4], 1),  # Cycle starts at index 1 (value 2)
    ([1, 2], 0),         # Cycle starts at index 0 (value 1)
    ([1], -1),           # No cycle
    ([1, 2, 3, 4], 2),   # Cycle starts at index 2 (value 3)
    ([], -1),            # Empty list
])

def test_detect_cycle(values, pos):
    head, expected_node = create_linked_list_with_cycle(values, pos)
    assert detect_cycle(head) == expected_node


# --- Execution Block ---
if __name__ == "__main__":
    # Use -v for verbose output and -p no:warnings to keep it clean
    pytest.main([__file__, "-v", "-p", "no:warnings"])