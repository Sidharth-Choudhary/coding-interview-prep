'''
Docstring for Algorithm.Week1.TwoPointers.2_remove-nth-node-from-end-of-list
Problem: Remove nth Node from End of List
Given the head of a singly linked list and an integer n, remove the nth node from the end of the list and return the head of the modified list.
Constraints:
1 ≤ number of nodes in the list ≤ k
1 ≤ n ≤ k
'''
import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(nodes):
    """Helper to convert array to Linked List"""
    dummy = ListNode(0)
    curr = dummy
    for val in nodes:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_array(head):
    """Helper to convert Linked List back to array for testing"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def removeNthFromEnd(head, n):
    left = head
    right = head
    
    for _ in range(n):
        right = right.next
        
    if not right:
        return head.next
    
    while right.next:
        right = right.next
        left = left.next
    
    left.next = left.next.next
    return head

# --- Pytest Parametrized Tests ---

@pytest.mark.parametrize("input_data, n, expected", [
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]), # Middle removal
    ([1, 2], 2, [2]),                   # Head removal
    ([1], 1, []),                      # Single node list
    ([1, 2, 3], 1, [1, 2]),             # Tail removal
])

def test_removeNthFromEnd(input_data, n, expected):
    # 1. Setup: Convert the input list to a Linked List
    head = to_list(input_data)

    # 2. Execution: Run your function
    result = removeNthFromEnd(head, n)

    # 3. Validation: Convert back to array and compare
    assert to_array(result) == expected

# --- This allows you to use 'python func.py' ---
if __name__ == "__main__":
    pytest.main([__file__, "-v", "-p", "no:warnings"])