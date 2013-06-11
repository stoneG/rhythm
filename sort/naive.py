from random import randint
import unittest

# Implementation of naive sort
# Runtime: O(n^2)
# Memory: O(1)

def naive_sort(values):
    """Returns the given list sorted."""
    for i, value_i in enumerate(values):
        minimum = value_i
        minimum_index = i
        for j, value_j in enumerate(values[i+1:]):
            if value_j <= minimum:
                minimum = value_j
                minimum_index = j + i + 1
        values[i], values[minimum_index] = values[minimum_index], values[i]
    return values

# Testing suite
class NaiveSortTest(unittest.TestCase):
    def setUp(self):
        self.random_list = [randint(-(2**7), (2**7) - 1) for i in range(1000)]

    def testSort(self):
        sorted_list = sorted(self.random_list)
        for i, value in enumerate(naive_sort(self.random_list)):
            self.assertEqual(value, sorted_list[i])

if __name__ == '__main__':
    unittest.main()
