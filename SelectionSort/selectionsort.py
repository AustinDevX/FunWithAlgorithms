import unittest
from typing import List, Sequence


class SelectionSortTests(unittest.TestCase):

    def test_returns_sorted_list(self):
        test_list = [10, 3, 42, 5, 68, 0, 39, -23, 4, -22]
        selection_sort(test_list)                 # the sorted test list

        sorted_list = [-23, -22, 0, 3, 4, 5, 10, 39, 42, 68]    # the correct sorted list

        for i in range(0, len(test_list)):
            self.assertEqual(test_list[i], sorted_list[i],
            'element {} at index {} in sorted test list does not match its correct position'. format(test_list[i], i))


def selection_sort(lst: List[int]):
    """ Sorts a list of integers in ascending order using the selection sort algorithm """
    for i in irange(0, len(lst) -2):
        min_index = i   # assume the current index corresponds to the index of the smallest element
        for j in irange(i, len(lst) -1):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]


def irange(start: int, end: int) -> Sequence[int]:
    """ Creates a sequence of integers from the 'start' parameter to the 'end' parameter inclusively """
    return range(start, end+1)
