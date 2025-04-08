import unittest
from test_search_methods import TestSearchMethods

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)