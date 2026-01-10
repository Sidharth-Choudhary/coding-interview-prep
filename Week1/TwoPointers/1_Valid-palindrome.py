''' Statement
Given a string, s, return TRUE if it is a palindrome; otherwise, return FALSE.

A phrase is considered a palindrome if it reads the same backward as forward after converting all uppercase letters to lowercase and removing any characters that are not letters or numbers. Only alphanumeric characters (letters and digits) are taken into account.

Constraints:
1≤ s.length ≤3000
s consists only of printable ASCII characters. '''

import pytest

def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -=1

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


# --- Pytest Parametrized Tests ---

@pytest.mark.parametrize("input_str, expected", [
    ("madam", True), # Test 1: Standard palindrome
    ("Step on no pets", True),# Test 2: Case sensitivity
    ("No 'x' in Nixon", True),# Test 3: Punctuation
    ("python", False), ## Test 4:Negative Cases
])

def test_is_palindrome(input_str, expected):
    assert is_palindrome(input_str) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-p", "no:warnings"])