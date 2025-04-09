class ForFunArray:
    def __init__(self):
        self.name = "ForFun"
        self.description = "This is a class for fun."
        self.version = "1.0.0"
        self.author = "Your Name"

    def greet(self):
        return f"Hello from {self.name}!"
    
    @classmethod
    def two_sum(cls, nums, target):
        """
        Returns the sum of two numbers.
        """
        lookup = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], i]
            lookup[num] = i
        return None
    @classmethod
    def max_sub_sum(cls, nums):
        """
        Returns the maximum subarray sum.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if all(num < 0 for num in nums):
            return max(nums)
        if all(num >= 0 for num in nums):
            return sum(nums)
        # Kadane's algorithm
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    @classmethod
    def move_zeros(cls, nums):
        """
        Moves all zeros to the end of the array."""
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        if all(num == 0 for num in nums):
            return nums
        if all(num != 0 for num in nums):
            return nums
        # Two-pointer approach
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
        return nums
    @classmethod
    def product_no_division(cls, nums):
        """
        Returns the product of all numbers in the array except the current number.
        Not using division.
        """
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)
        for i in range(1, len(nums)):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
        result = []
        for i in range(len(nums)):
            result.append(left_products[i] * right_products[i])
        return result
    @classmethod
    def rotate_array(cls, nums, k):
        """
        Rotates the array to the right by k steps.
        """
        if not nums:
            return []
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
        return nums
    

class ForFunString:
    def __init__(self):
        self.name = "ForFun"
        self.description = "This is a class for fun."
        self.version = "1.0.0"
        self.author = "Your Name"

    def greet(self):
        return f"Hello from {self.name}!"
    
    @classmethod
    def reverse_string(cls, s):
        """
        Reverses the given string.
        """
        return s[::-1]
    @classmethod
    def check_anagram(cls, s1, s2):
        """
        Checks if two strings are anagrams.
        """
        return sorted(s1) == sorted(s2)
    @classmethod
    def get_longest_sub_string(cls, s):
        """
        Returns the longest substring without repeating characters.
        """
        char_index = {}
        start = max_length = 0
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_length = max(max_length, i - start + 1)
        return max_length