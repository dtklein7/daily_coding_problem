"""Note: potentially could get speedup with sorted list,
pulling from back...
"""

from typing import List, Optional


def mix_chars(s: str) -> Optional[str]:
    """Mutates string such that no two adjascent characters are alike.

    Worst case: O(N^2)
    Best case: O(N)

    Returns:
        str: mutation possible
        None: mutation impossible
    """
    l = list(s)
    # iterate through tokenized string
    for i in range(len(l) - 1):
        # if adjascent chars equal, swap to next non-equal char
        if l[i] == l[i + 1]:
            # if no nonequal character exists to swap with, return None
            try:
                swap_idx = _get_next_noneqal_char(l, i + 1)
            except IndexError:
                return None
            l = _swap_chars(l, i+1, swap_idx)

    return str(l)


def _get_next_noneqal_char(l: List[str], idx: int) -> int:
    not_this_char = l[idx]
    while True:
        if l[idx] != not_this_char:
            return idx
        idx += 1


def _swap_chars(l: List[str], idx: int, swap_idx: int):
    temp = l[idx]
    l[idx] = l[swap_idx]
    l[swap_idx] = temp
    return l
