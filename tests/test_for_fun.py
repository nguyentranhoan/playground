from algorithms.for_fun import ForFunArray
import unittest

class TestForFunArray(unittest.TestCase):    
    def setUp(self):
        self.for_fun = ForFunArray()

    def test_greet(self):
        self.assertEqual(self.for_fun.greet(), "Hello from ForFunArray!")

    def test_two_sum(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_result = [0, 1]
        self.assertEqual(ForFunArray.two_sum(nums, target), expected_result)
    def test_two_sum_no_solution(self):
        nums = [1, 2, 3]
        target = 6
        expected_result = None
        self.assertEqual(ForFunArray.two_sum(nums, target), expected_result)
    def test_two_sum_empty_list(self):
        nums = []
        target = 0
        expected_result = None
        self.assertEqual(ForFunArray.two_sum(nums, target), expected_result)
    def test_two_sum_one_element(self):
        nums = [1]
        target = 1
        expected_result = None
        self.assertEqual(ForFunArray.two_sum(nums, target), expected_result)
    def test_two_sum_same_numbers(self):
        nums = [1, 1, 2]
        target = 2
        expected_result = [0, 1]
        self.assertEqual(ForFunArray.two_sum(nums, target), expected_result)
    def test_max_sub_sum(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_result = 6
        self.assertEqual(ForFunArray.max_sub_sum(nums), expected_result)
    def test_max_sub_sum_empty_list(self):
        nums = []
        expected_result = 0
        self.assertEqual(ForFunArray.max_sub_sum(nums), expected_result)
    def test_max_sub_sum_single_element(self):
        nums = [5]
        expected_result = 5
        self.assertEqual(ForFunArray.max_sub_sum(nums), expected_result)
    def test_move_zeros(self):
        nums = [0, 1, 0, 3, 12]
        expected_result = [1, 3, 12, 0, 0]
        self.assertEqual(ForFunArray.move_zeros(nums), expected_result)
    def test_move_zeros_empty_list(self):
        nums = []
        expected_result = []
        self.assertEqual(ForFunArray.move_zeros(nums), expected_result)
    def test_product_no_division(self):
        nums = [1, 2, 3, 4]
        expected_result = [24, 12, 8, 6]
        self.assertEqual(ForFunArray.product_no_division(nums), expected_result)
    def test_product_no_division_empty_list(self):
        nums = []
        expected_result = []
        self.assertEqual(ForFunArray.product_no_division(nums), expected_result)
    def test_rotate_array(self):
        nums = [1, 2, 3, 4, 5]
        k = 2
        expected_result = [4, 5, 1, 2, 3]
        self.assertEqual(ForFunArray.rotate_array(nums, k), expected_result)
if __name__ == "__main__":
    unittest.main()