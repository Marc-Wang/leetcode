#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return method1(nums, target)
        return method3(nums, target)

# def method1(nums, target):
#     '''time: O(n^2)  space: O(1)
#     29/29 cases passed (4304 ms)
#     Your runtime beats 11.26 % of python submissions
#     Your memory usage beats 6.17 % of python submissions (13.5 MB)
#     '''
#     for i, valuei in enumerate(nums):
#         for j, valuej in enumerate(nums):
#             if valuei + valuej == target and i != j:
#                 return [i, j]
def method1(nums, target):
    ''' O(n^2) 
    29/29 cases passed (5588 ms)
    Your runtime beats 19.07 % of python3 submissions
    Your memory usage beats 13.41 % of python3 submissions (14.6 MB)
    '''
    m = len(nums)
    for i in range(m):
        for j in range(i+1, m):
            if nums[i] + nums[j] == target:
                return [i, j]

def method2(nums, target):
    ''' time: O(n) space: O(n)
    use hash table, trade space for time
    29/29 cases passed (68 ms)
    Your runtime beats 55.29 % of python3 submissions
    Your memory usage beats 5.48 % of python3 submissions (15.2 MB)
    '''
    d = {}
    for i, v in enumerate(nums):
        d[v] = i
    for i in range(len(nums)):
        value = target - nums[i] 
        if value in d and i != d[value]:
            return [i, d[value]]

def method3(nums, target):
    ''' improvment of method2
    29/29 cases passed (64 ms)
    Your runtime beats 60.07 % of python3 submissions
    Your memory usage beats 5.48 % of python3 submissions (15.2 MB)
    '''
    d = {}
    n = len(nums)
    for i in range(n):
        if target-nums[i] in d:
            return [d[target-nums[i]], i]
        else:
            d[nums[i]] = i
# @lc code=end

