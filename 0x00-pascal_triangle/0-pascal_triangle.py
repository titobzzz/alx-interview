#!/usr/bin/python3
'''Pascal's triangle'''


def pascal_triangle(n):
    '''returnsa list of lists for integers representing the Pascal's-triangle
        of height: n.
       Returns an empty list if n < 1
       n will always be an integer
    '''
    if n < 1:
        return []

    triangle = [[1]]  # first-row is always just 1

    for row in range(1, n):
        inner = [1]   # first item in every row is always 1
        for col in range(1, row):
            #  thefirst and last items, an item at an index i in a given
            # row isequal to the sum of the items at indices i and (i - 1) in
            # the previous row
            inner.append(triangle[row - 1][col] + triangle[row - 1][col - 1])

        inner.append(1)  # last item in every row is always 1
        triangle.append(inner)

    return triangle
