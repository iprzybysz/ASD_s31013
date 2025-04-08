import time
import unittest

from search_methods import binary_search, jump_k

import unittest

class TestSearchMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up data before all tests"""
        cls.sorted_array = [-6, 1, 2, 8, 9, 10, 12, 15, 16]
        cls.empty_array = []
        cls.single_element_array = [2]
        cls.large_array = list(range(1_000_000))

        cls.target_index = 4
        cls.target_element = cls.sorted_array[cls.target_index]
        cls.target_large_element = 1

        cls.non_existent_index = -1
        cls.non_existent_element = 1910

        cls.first_element = cls.sorted_array[0]
        cls.last_element = cls.sorted_array[-1]

    def test_binary_search_element_found(self):
        """Test if binary_search finds the target element in the sorted array"""
        self.assertEqual(binary_search(self.sorted_array, self.target_element), self.target_index)

    def test_binary_search_element_not_found(self):
        """Test if binary_search returns -1 when the target element is not in the array"""
        self.assertEqual(binary_search(self.sorted_array, self.non_existent_element), self.non_existent_index)

    def test_binary_search_element_as_first(self):
        """Test if binary_search returns 0 when the target element is the first in the sorted array"""
        self.assertEqual(binary_search(self.sorted_array, self.first_element), 0)

    def test_binary_search_element_as_last(self):
        """Test if binary_search returns the last index when the target element is the last in the sorted array"""
        self.assertEqual(binary_search(self.sorted_array, self.last_element), len(self.sorted_array) - 1)

    def test_binary_search_empty_array(self):
        """Test if binary_search returns -1 for an empty array"""
        self.assertEqual(binary_search(self.empty_array, self.target_element), -1)

    def test_binary_search_single_element_array(self):
        """Test if binary_search returns 0 for an array with one element"""
        self.assertEqual(binary_search(self.single_element_array, self.single_element_array[0]), 0)

    def test_jump_k_element_found(self):
        """Test if jump_k finds the target element in the sorted array"""
        self.assertEqual(jump_k(self.sorted_array, self.target_element), self.target_index)

    def test_jump_k_element_not_found(self):
        """Test if jump_k returns -1 when the target element is not in the array"""
        self.assertEqual(jump_k(self.sorted_array, self.non_existent_element), self.non_existent_index)

    def test_jump_k_element_as_first(self):
        """Test if jump_k returns 0 when the target element is the first in the sorted array"""
        self.assertEqual(jump_k(self.sorted_array, self.first_element), 0)

    def test_jump_k_element_as_last(self):
        """Test if jump_k returns the last index when the target element is the last in the sorted array"""
        self.assertEqual(jump_k(self.sorted_array, self.last_element), len(self.sorted_array) - 1)

    def test_jump_k_empty_array(self):
        """Test if jump_k returns -1 for an empty array"""
        self.assertEqual(jump_k(self.empty_array, self.target_element), -1)

    def test_jump_k_single_element_array(self):
        """Test if jump_k returns 0 for an array with one element"""
        self.assertEqual(jump_k(self.single_element_array, 2), 0)

    def test_binary_search_vs_jump_k_performance(self):
        """Compare the performance of binary_search and jump_k on the same array"""
        
        start_time = time.time()
        binary_search_result = binary_search(self.sorted_array, self.target_large_element)
        end_time = time.time()
        binary_search_elapsed_time = end_time - start_time
        
        start_time = time.time()
        jump_k_result = jump_k(self.sorted_array, self.target_large_element)
        end_time = time.time()
        jump_k_elapsed_time = end_time - start_time

        self.assertEqual(binary_search_result, jump_k_result, "Results of binary_search and jump_k do not match")
        
        print(f"binary_search elapsed time: {binary_search_elapsed_time:.6f} seconds")
        print(f"jump_k elapsed time: {jump_k_elapsed_time:.6f} seconds")
        
        self.assertLess(binary_search_elapsed_time, jump_k_elapsed_time, "binary_search is slower than jump_k")