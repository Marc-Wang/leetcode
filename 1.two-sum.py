#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return s1(nums, target)
# @lc code=end

# solutions
def s1(nums: list[int], target: int):
    myhash = {}
    for key in nums:
        print(key)

# test
nums = [2,7,11,15] 
target = 9
print(s1(nums, target))
help('os')