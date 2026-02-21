#!/usr/bin/env python3
"""a function that concatenates two
matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices along a specific axis"""
    def _is_valid_matrix(mat):
        if not isinstance(mat, list) or len(mat) == 0:
            return False
        # all rows must be lists and have same length > 0
        if any(not isinstance(row, list) for row in mat):
            return False
        row_len = len(mat[0])
        # allow zero-length rows (0 columns); ensure all rows have same length
        for row in mat:
            if len(row) != row_len:
                return False
            # only check element types when there are columns
            if row_len > 0:
                for el in row:
                    if not isinstance(el, (int, float)):
                        return False
        return True

    if not _is_valid_matrix(mat1) or not _is_valid_matrix(mat2):
        return None

    if axis not in (0, 1):
        return None

    if axis == 0:
        # vertical concat: number of columns must match
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    # axis == 1: horizontal concat: number of rows must match
    if len(mat1) != len(mat2):
        return None
    return [r1 + r2 for r1, r2 in zip(mat1, mat2)]
