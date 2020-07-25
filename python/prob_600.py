"""Problem 600: closest points

given a list of 2-int tuples, return the two closest points.

Notes:
    I think we have to compare all points, so O(N^2) is best-case

    edit: hmm we dont have to re-compare, so maybe it's less than O(N^2)...
"""

import math

TEST_CASES = [
    [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)],
]


def dist_between_tups(tup_a, tup_b):
    return math.sqrt((tup_b[0] - tup_a[0])**2 + (tup_b[1] - tup_a[1])**2)

def find_closest_points(points):
    closest = math.inf
    return_tup_a, return_tup_b = [(None, None), (None, None)]
    for i, point in enumerate(points):
        for comparison in points[i + 1:]:
            dist = dist_between_tups(point, comparison)
            if dist < closest:
                closest = dist
                return_tup_a, return_tup_b = point, comparison
    
    return return_tup_a, return_tup_b

if __name__ == "__main__":
    print(find_closest_points(TEST_CASES[0]))
