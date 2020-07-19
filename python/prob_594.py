"""Problem 594: Boggle! 

You are given an N by N matrix of random letters and a dictionary of words.
Find the maximum number of words that can be packed on the board from the
given dictionary.

words = { 'eat', 'rain', 'in', 'rat' }

dict = [
    ['e', 'a', 'n'],
    ['t', 't', 'i'],
    ['a', 'r', 'a']
]

res =  3 ('eat', 'in', and 'rat')"""

from typing import List, Set, Tuple
from collections import Counter

TEST_CASES: List[Tuple[Set[str], List[List[str]]]] = [
    (   
        { 'eat', 'rain', 'in', 'rat' },
        [
            ['e', 'a', 'n'],
            ['t', 't', 'i'],
            ['a', 'r', 'a']
        ]
    )
]

def boggle(words, letter_matrix):
    letter_bank = Counter()
    for row in letter_matrix:
        letter_bank += Counter(row)

    res = 0
    for word in sorted(list(words), key=len):
        bank_cache = letter_bank.copy()
        _find_counts()



if __name__ == '__main__':
    for test in TEST_CASES:
        boggle(test[0], test[1])
