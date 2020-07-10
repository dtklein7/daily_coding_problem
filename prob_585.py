""" problem 585 - UNFINISHED

'Given an N by M matrix consisting only of 1's and 0's,
find the largest rectangle containing only 1's and return its area.'

Not a great solution, worse than O(N*M)
"""

def largest_rect(nm_matrix):
    curr_largest_rect = 0
    bounds = (len())
    for row in nm_matrix:
        for col in row:
            if col == 1:
                curr_largest_rect = max(
                    curr_largest_rect,
                    _get_rect_size(nm_matrix, row, col)
                )

    return curr_largest_rect


def _get_rect_size(nm_matrix, row, col):
    max_x, max_y = 0, 0
    orig_x, orig_y = row, col
    coords = {'x': row, 'y': col}

    # find x bound
    while (nm_matrix[coords['x']][coords['y']] != 0) and :
        coords['x'] += 1
        max_x += 1
    # check all y vals
    for x in range(orig_x, coords['x'] + 1):
        while (nm_matrix[coords['x']][coords['y']] != 0) and :



if __name__ == '__main__':
    sample = [[1, 0, 0, 0],
              [1, 0, 1, 1],
              [1, 0, 1, 1],
              [0, 1, 0, 0]]
    largest_rect(sample)
