"""
Two Sum Problem

Problem:
Given an array of integers nums and an integer target, 
return the indices of the two numbers that add up to the target.
You may not use the same element twice.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] == 9, so we return [0, 1].
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Dictionary to store the value and its index
    seen = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if complement exists in the dictionary
        if complement in seen:
            return [seen[complement], i]
        
        # Store the current number and its index
        seen[num] = i
    
    # If no two numbers add up to target
    return []


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {twoSum(nums1, target1)}")  # Expected: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"\nInput: nums = {nums2}, target = {target2}")
    print(f"Output: {twoSum(nums2, target2)}")  # Expected: [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"\nInput: nums = {nums3}, target = {target3}")
    print(f"Output: {twoSum(nums3, target3)}")  # Expected: [0, 1]
    
    # Test case 4 - No solution
    nums4 = [1, 2]
    target4 = 10
    print(f"\nInput: nums = {nums4}, target = {target4}")
    print(f"Output: {twoSum(nums4, target4)}")  # Expected: []
