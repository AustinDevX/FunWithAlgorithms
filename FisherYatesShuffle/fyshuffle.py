from    typing import List
import  unittest
import  pdb

import random

def fyshuffle(l: List[int]):
    """ Performs a modern fisher yates shuffle on an array of integers """
    for curr_index in range(0, len(l) - 1):
        dest_index = random.randint(curr_index, len(l)-1)
        # perform a bitswap on the integer values
        l[curr_index] = l[curr_index] ^ l[dest_index]
        l[dest_index] = l[curr_index] ^ l[dest_index]
        l[curr_index] = l[curr_index] ^ l[dest_index]

class shuffleTest(unittest.TestCase):
    def test_shuffles_array(self):
        """ From the above algorithm since each destination index is selected from
            the range of the current index to the last index it is possible that
            the all elements in the test array may end up in the same position in
            which case the test may fail"""

        comparison_array = [1, 2, 3, 4, 5]
        shuffled_array   = comparison_array[:]
        fyshuffle(shuffled_array)
        self.assertNotEqual(comparison_array, shuffled_array, 'Array has not been shuffled')

# TODO: Implement a type generic fyshuffle
