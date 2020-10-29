"""
Given an integer n and a list of integers l,
write a function that randomly generates a number
from 0 to n-1 that isn't in l (uniform).

Opening thoughts:
    What does uniform mean?
        all distinct probabilities are equally likely
    Is it useful to sort the list?
        probably - we can prune the list in o(N)
    Will negative numbers mess this up?
        no! not if we don't let them :)
    Sets - what does access time cost? i.e., how expensive is it to check if something is in a set?
        probably more expensive than checking by index.
"""

from typing import List
import random
import timeit


TEST_CASES = [
    {'n': 3, 'l': [1, 2, 3, 4, 5], 'possible_ans': [0]},
    {'n': 7, 'l': [1, 2, 4, 6, 7], 'possible_ans': [0, 3, 5]},
    {'n': 4, 'l': [-30, 225, 1, 0, 7, 7, 7], 'possible_ans': [2, 3]},
    {'n': 6, 'l': [-2, -1, -1, 1, 3, 2], 'possible_ans': [0, 2, 4, 5]},
]


def old_return_rand(n: int, l: List[int]) -> int:  # noqa: E741
    """O(l^2)"""
    dangerous_set = set(l)
    possible_nums = set()
    for num in range(n):
        if num >= 0 and num not in dangerous_set:
            possible_nums.add(num)
    if len(possible_nums) == 0:
        return -1
    return list(possible_nums)[random.randint(0, len(possible_nums) - 1)]


def return_rand(n: int, l: List[int]) -> int:  # noqa: E741
    """theoretically O(l*log(l)), but slower! Ugh..."""
    l_idx = 0
    possible_nums = set()
    l = sorted(l)

    for num in range(n):
        while num > l[l_idx]:
            if l_idx >= len(l) - 1:
                break
            l_idx += 1

        if l[l_idx] != num:
            possible_nums.add(num)

    if len(possible_nums) == 0:
        return -1

    return list(possible_nums)[random.randint(0, len(possible_nums) - 1)]


if __name__ == "__main__":
    for tc in TEST_CASES:
        t1 = timeit.timeit('old_return_rand(tc["n"], tc["l"])', globals=globals())
        t2 = timeit.timeit('return_rand(tc["n"], tc["l"])', globals=globals())

        print(f'average first_implementation time for input {tc}:\n{t1}\n')
        print(f'average second_implementation time for input {tc}:\n{t2}\n')
