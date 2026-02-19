#!/usr/bin/env python3
""" Write a function that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise"""
    if type(arr1) is not list or type(arr2) is not list:
        return None
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
