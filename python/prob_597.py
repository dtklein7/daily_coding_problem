"""Problem 597: Pythagorean Triplets."""

TEST_CASES = [
    (1, 2, 3),
    (8, 1, 10),
    (4, 5, 6)
]


def is_pythag(tup):
    for i in tup:
        idx_a = indicies[:].pop()
        idx_b = indicies.copy().remove(i)[-1]
        if tup[:]**2 + tup[idx_b]**2 == tup[i]**2:
            return True
    return False


if __name__ == "__main__":
    for test_case in TEST_CASES:
        res = is_pythag(test_case)
        print(f'{test_case}\n{res}\n')