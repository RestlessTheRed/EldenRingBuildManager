from bisect import bisect_left
from typing import List


def find_closest(array: List[int], number: int):
    pos = bisect_left(array, number)
    if pos == 0:
        return array[0]
    if pos == len(array):
        return array[-1]
    before = array[pos - 1]
    after = array[pos]
    if after - number < number - before:
        return after
    else:
        return before
