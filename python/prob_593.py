"""Problem 593: Setting Sun

You are given an array representing the heights of neighboring buildings on a city
street, from east to west. The city assessor would like you to write an algorithm
that returns how many of these buildings have a view of the setting sun, in order
to properly value the street.
"""

TEST_CASES = [
    [3, 4, 5, 6, 7, 8, 9],  # 7
    [9, 1, 2, 3, 4, 5, 6, 10],  # 2
    [1, 9, 1, 9, 1, 9, 1000],  # 3
]


def good_view_counts(buildings):
    max_height = 0
    res = 0

    for height in buildings:
        if height > max_height:
            res += 1
            max_height = height

    return res


if __name__ == "__main__":
    for building in TEST_CASES:
        print(good_view_counts(building))
