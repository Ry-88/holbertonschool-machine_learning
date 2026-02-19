#!/usr/bin/env python3
""" a function that concatenates two arrays"""


def cat_arrays(arr1, arr2):
    """concatenates tow arrays"""
    if type(arr1) is not list or type(arr2) is not list:
        return None
    return arr1 + arr2
