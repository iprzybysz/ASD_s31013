import unittest
from test_sort_algorithms import TestSortAlgorithms

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortAlgorithms)
    unittest.TextTestRunner(verbosity=2).run(suite)