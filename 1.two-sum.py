#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return basic(nums, target)
        # return hash(nums, target)




def basic(nums, target):
    # nested 2 for loop 
    # O(n^2)
    for i in range(10):
        for j in range(i+1, 10):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [0, 0]

# def hash(nums, target):

# @lc code=end

