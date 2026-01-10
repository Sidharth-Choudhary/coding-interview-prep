### Problem: Linked List Cycle IV

'''
Statement
Given the head of a singly linked list, implement a function to detect and remove any cycle present in the list. A cycle occurs when a node's next pointer links back to a previous node, forming a loop within the list.

The function must modify the linked list in place, ensuring it remains acyclic while preserving the original node order. If no cycle is found, return the linked list as is.

Constraints:
    1) The number of nodes in the list is in the range [0,10^4].
    2) −10^5≤ Node.value ≤ 10^5
'''
import pytest

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

# Helper function to convert linked list to a Python list for testing
def linked_list_to_list(head: ListNode) -> list:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
###############################################################

def detect_and_remove_cycle(head):
    slow = head
    fast = head
    has_cycle = False
    if not head and not head.next:
        return head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return head

    slow = head

    while (slow != fast):
        slow = slow.next
        fast = fast.next

    while (fast.next != slow):
        fast = fast.next

    fast.next = None

    return head

###############################################################

# cycle_pos is 0-indexed; -1 means no cycle
test_data = [
    ([3, 2, 0, -4], 1, [3, 2, 0, -4]),  # Cycle to node with value 2
    ([1, 2], 0, [1, 2]),  # Cycle to node with value 1
    ([1], -1, [1]),  # No cycle, single node
    ([1, 2, 3, 4, 5], -1, [1, 2, 3, 4, 5]),  # No cycle, multiple nodes
    ([1, 2, 3], 2, [1, 2, 3])  # Cycle to node with value 3 (last node points to itself)
]


@pytest.mark.parametrize("values, cycle_pos, expected", test_data)
def test_detect_and_remove_cycle(values, cycle_pos, expected):
    # Setup linked list
    if not values:
        head = None
    else:
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        # Create cycle if pos is valid
        if cycle_pos != -1:
            nodes[-1].next = nodes[cycle_pos]
        else:
            nodes[-1].next = None  # Ensure the last node points to None for no-cycle case

        head = nodes[0]

    # Run the function
    result_head = detect_and_remove_cycle(head)

    # Verify the result
    actual_list = linked_list_to_list(result_head)
    assert actual_list == expected

    # Also verify that after removal, there is indeed no cycle using the function itself
    # A list with no cycle will return the original list, so this is covered by the above
    # A more robust check might involve traversing and using a set to ensure no cycles exist in the *returned* list structure.
    visited = set()
    current = result_head
    while current:
        assert current not in visited, "Cycle still exists after removal!"
        visited.add(current)
        current = current.next

# --- Execution Block ---
if __name__ == "__main__":
    # Use -v for verbose output and -p no:warnings to keep it clean
    pytest.main([__file__, "-v", "-p", "no:warnings"])