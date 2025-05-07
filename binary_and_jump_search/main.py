import unittest
from test_search_algorithms import TestSearchAlgorithms

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchAlgorithms)
    unittest.TextTestRunner(verbosity=2).run(suite)