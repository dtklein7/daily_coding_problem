"""Problem 633: near-sort

You are given a list of N numbers, in which each number
is located at most k places away from its sorted position.

For example, if k = 1, a given element at index 4
might end up at indices 3, 4, or 5.
"""

TEST_CASE = {
    'lis': [1, 2, 3, 5, 4, 7, 6, 6],
    'k': 2
}


def main(lis, k):
    prev = lis[0]
    idx = 1
    while idx < len(lis):
        if lis[idx] < prev:
            lis = _fix(idx, lis, k)
        prev = lis[idx]
        idx += 1
    return lis


def _fix(idx, lis, k):
    for i in range(k):
        if lis[idx] < lis[idx-i-1]:
            return _swap(lis, idx, idx-i-1)
    raise RuntimeError('you lied!')


def _swap(lis, idx1, idx2):
    temp = lis[idx1]
    lis[idx1] = lis[idx2]
    lis[idx2] = temp
    return lis


if __name__ == "__main__":
    print(main(**TEST_CASE))