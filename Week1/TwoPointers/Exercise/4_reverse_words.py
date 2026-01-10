### Problem: Reverse Words in a String

'''
Statement
You are given a string sentence that may contain leading or trailing spaces, as well as multiple spaces between words. Your task is to reverse the order of the words in the sentence without changing the order of characters within each word. Return the resulting modified sentence as a single string with words separated by a single space, and no leading or trailing spaces.

Note: A word is defined as a continuous sequence of non-space characters. Multiple words separated by single spaces form a valid English sentence. Therefore, ensure there is only a single space between any two words in the returned string, with no leading, trailing, or extra spaces.

Input -- "Smart"
Output -- "Smart"

Input -- "Reverse this string"
Output -- "string this Reverse"

Input -- "  Multiple   Spaces   "
Outpyt -- "Spaces Multiple"

Input -- "I have 3 cats and 1 dog"
Output -- "dog 1 and cats 3 have I"
'''

import pytest

def reverse_words(sentence):

    ## Write your code here

    return


# --- Pytest Parametrized Tests ---

@pytest.mark.parametrize("input_str, expected", [
    ("hello world", "world hello"),
    ("  space  test  ", "test space"),
    ("single", "single"),
    ("", ""),
    ("1 2 3 4", "4 3 2 1"),
    ("Multiple   Spaces", "Spaces Multiple"),
])

def test_reverse_words(input_str, expected):
    assert reverse_words(input_str) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-p", "no:warnings"])