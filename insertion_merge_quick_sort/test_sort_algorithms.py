import time
import unittest
from sorting_algorithms import insertion_sort, merge_sort, quicksort


class TestSortAlgorithms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up data before all tests"""
        cls.unsorted_array = [64, 34, 25, 12, 22, 11, 90]
        cls.sorted_array = [11, 12, 22, 25, 34, 64, 90]
        cls.empty_array = []
        cls.single_element_array = [42]
        cls.reversed_array = [90, 64, 34, 25, 22, 12, 11]
        cls.duplicate_array = [1, 4, 2, 4, 2, 4, 1, 2, 3]
        cls.large_array = list(range(500, 0, -1))  
        
    def setUp(self):
        """Reset arrays before each test"""
        self.test_array = self.unsorted_array.copy()
        self.test_reversed = self.reversed_array.copy()
        self.test_duplicate = self.duplicate_array.copy()
    
    def test_insertion_sort_basic(self):
        """Test if insertion_sort correctly sorts a basic unsorted array"""
        result = insertion_sort(self.test_array)
        self.assertEqual(result, self.sorted_array)

    def test_insertion_sort_empty(self):
        """Test if insertion_sort handles empty array correctly"""
        result = insertion_sort(self.empty_array.copy())
        self.assertEqual(result, [])

    def test_insertion_sort_single_element(self):
        """Test if insertion_sort handles single element array correctly"""
        result = insertion_sort(self.single_element_array.copy())
        self.assertEqual(result, self.single_element_array)

    def test_insertion_sort_reversed(self):
        """Test if insertion_sort handles reversed array correctly"""
        result = insertion_sort(self.test_reversed)
        self.assertEqual(result, self.sorted_array)

    def test_insertion_sort_duplicates(self):
        """Test if insertion_sort handles array with duplicates correctly"""
        result = insertion_sort(self.test_duplicate)
        self.assertEqual(result, sorted(self.test_duplicate))

    def test_merge_sort_basic(self):
        """Test if merge_sort correctly sorts a basic unsorted array"""
        result = merge_sort(self.test_array)
        self.assertEqual(result, self.sorted_array)

    def test_merge_sort_empty(self):
        """Test if merge_sort handles empty array correctly"""
        result = merge_sort(self.empty_array.copy())
        self.assertEqual(result, [])

    def test_merge_sort_single_element(self):
        """Test if merge_sort handles single element array correctly"""
        result = merge_sort(self.single_element_array.copy())
        self.assertEqual(result, self.single_element_array)

    def test_merge_sort_reversed(self):
        """Test if merge_sort handles reversed array correctly"""
        result = merge_sort(self.test_reversed)
        self.assertEqual(result, self.sorted_array)

    def test_merge_sort_duplicates(self):
        """Test if merge_sort handles array with duplicates correctly"""
        result = merge_sort(self.test_duplicate)
        self.assertEqual(result, sorted(self.test_duplicate))

    def test_quicksort_basic(self):
        """Test if quicksort correctly sorts a basic unsorted array"""
        test_array = self.test_array.copy()
        quicksort(test_array, 0, len(test_array) - 1)
        self.assertEqual(test_array, self.sorted_array)

    def test_quicksort_empty(self):
        """Test if quicksort handles empty array correctly"""
        test_array = self.empty_array.copy()
        quicksort(test_array, 0, len(test_array) - 1)
        self.assertEqual(test_array, [])

    def test_quicksort_single_element(self):
        """Test if quicksort handles single element array correctly"""
        test_array = self.single_element_array.copy()
        quicksort(test_array, 0, len(test_array) - 1)
        self.assertEqual(test_array, self.single_element_array)

    def test_quicksort_reversed(self):
        """Test if quicksort handles reversed array correctly"""
        test_array = self.test_reversed.copy()
        quicksort(test_array, 0, len(test_array) - 1)
        self.assertEqual(test_array, self.sorted_array)

    def test_quicksort_duplicates(self):
        """Test if quicksort handles array with duplicates correctly"""
        test_array = self.test_duplicate.copy()
        quicksort(test_array, 0, len(test_array) - 1)
        self.assertEqual(test_array, sorted(self.test_duplicate))

    def test_sorting_algorithms_performance(self):
        """Compare the performance of all sorting algorithms on a large array"""
        expected_sorted = sorted(self.large_array)
        
        large_array_insertion = self.large_array.copy()
        large_array_merge = self.large_array.copy()
        large_array_quick = self.large_array.copy()
        
        start_time = time.time()
        insertion_sort(large_array_insertion)
        insertion_sort_time = time.time() - start_time
        
        start_time = time.time()
        large_array_merge = merge_sort(large_array_merge)  
        merge_sort_time = time.time() - start_time
        
        start_time = time.time()
        quicksort(large_array_quick, 0, len(large_array_quick) - 1)
        quicksort_time = time.time() - start_time

        print(f"\nPerformance test results for {len(self.large_array)} elements:")
        print(f"Insertion Sort time: {insertion_sort_time:.6f} seconds")
        print(f"Merge Sort time: {merge_sort_time:.6f} seconds")
        print(f"Quick Sort time: {quicksort_time:.6f} seconds")

        self.assertEqual(large_array_insertion, expected_sorted)
        self.assertEqual(large_array_merge, expected_sorted)
        self.assertEqual(large_array_quick, expected_sorted)
        