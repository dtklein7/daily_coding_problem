"""Finding Islands.

Given a matrix of 1s and 0s, return the number of "islands"
in the matrix. A 1 represents land and 0 represents water,
so an island is a group of 1s that are neighboring whose
perimeter is surrounded by water.

e.g.: this matrix has four islands:

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""

import numpy as np

TEST_CASE = np.array([
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
])


def count_islands(arr: np.array):
    coord_cache = {}
    islands = 0

    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if (
                arr[row][col] == 1 and
                (row, col) not in coord_cache
            ):
                islands += 1
                coord_cache = _check_for_island(
                    coord_cache, arr, row, col
                )

    return islands


def _check_for_island(coord_cache, arr, row, col, check_left=False):
    """Check and cache for islands.
    This implementation must be an antipattern..."""
    # check right
    if col < len(arr[0]) - 1 and arr[row][col + 1] == 1:
        coord_cache[(row, col + 1)] = True
        coord_cache = _check_for_island(
            coord_cache, arr, row, col + 1, False)
    else:
        coord_cache[(row, col + 1)] = False
    # check down
    if row < len(arr) - 1 and arr[row + 1][col] == 1:
        coord_cache[(row + 1, col)] = True
        coord_cache = _check_for_island(
            coord_cache, arr, row + 1, col, True)
    else:
        coord_cache[(row + 1, col)] = False
    # check left
    if check_left:
        if col > 0 and arr[row][col - 1] == 1:
            coord_cache[(row, col - 1)] = True
            coord_cache = _check_for_island(
                coord_cache, arr, row, col - 1, True)
        else:
            coord_cache[(row, col - 1)] = False

    return coord_cache


if __name__ == "__main__":
    print(count_islands(TEST_CASE))
