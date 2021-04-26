#! /usr/bin/python3.6
"""
Twig coding challenge:

Given an array of length >= 0, and a positive integer N, return the contents
of the array divided into N equally sized arrays.

Where the size of the original array cannot be divided equally by N,
the final part should have length equal to the remainder.
"""

import math


def split_list(original_list, number_of_new_lists):
    """
    Splits a list in to a specified number of sub-lists.

    Args:
        original_list: The original list to be split.
        number_of_new_lists: The number of new lists to create.

    Returns:
        A list of lists.
    """
    try:
        new_lists_size = math.ceil(len(original_list) / number_of_new_lists)
        return [original_list[i:i+new_lists_size]
                for i in range(0, len(original_list), new_lists_size)]
    except (ZeroDivisionError, ValueError):
        return []
