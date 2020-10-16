"""
Given a list of elements, find the majority element,
which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.

Notes:
    This soultion is hacky as heck, but quite readable!
    I wonder if there's a way to do this without reading the whole list...
        Proposal:
            iterate through list, once an element has count > floor(len(lst) / 2.0),
            return that element/.

        Conclusion:
            second method is 4x faster for given inputs!

            average first_implementation time for input [1, 2, 1, 1, 3, 4, 0]:
            12.505348900000001

            average second_implementation time for input [1, 2, 1, 1, 3, 4, 0]:
            3.4204808999999994

            average first_implementation time for input [420, 2, 420, 420, 3, 4, 0]:
            12.4518493

            average second_implementation time for input [420, 2, 420, 420, 3, 4, 0]:
            3.413398700000002
"""

from collections import Counter
import timeit
import math

TEST_CASES = [
    [1, 2, 1, 1, 3, 4, 0],
    [420, 2, 420, 420, 3, 4, 0],
]

def first_implementation(elements):
    return Counter(tc).most_common(1)[0][0]


def second_implementation(elements):
    threshhold = math.floor(len(elements) / 2.0)
    counts = {}
    for i in elements:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
        if counts[i] >= threshhold:
            return i
    raise RuntimeError('elements doesnt have a majority element!')

if __name__ == "__main__":
    for tc in TEST_CASES:
        first_time = timeit.timeit('first_implementation(tc)', globals=globals())
        second_time = timeit.timeit('second_implementation(tc)', globals=globals())
        print(f'average first_implementation time for input {tc}:\n{first_time}\n')
        print(f'average second_implementation time for input {tc}:\n{second_time}\n')

