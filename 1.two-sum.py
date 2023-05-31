#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return basic(nums, target)
        return hash(nums, target)




def basic(nums, target):
    # nested 2 for loop 
    # O(n^2)
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [0, 0]

def hash(nums, target):
    # use hash table
    # O()
    
# @lc code=end

