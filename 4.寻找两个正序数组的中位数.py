#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return basic(nums1, nums2)

def method1(nums1, nums2):
    '''time: O(m+n), space: O(m+n)
    2085/2085 cases passed (68 ms)
    Your runtime beats 44.61 % of python3 submissions
    Your memory usage beats 6.15 % of python3 submissions (13.5 MB'''
    nums = []
    length1 = len(nums1)
    length2 = len(nums2)
    times = length1 + length2
    for i in range(times):
        if length1 == 0:
            nums.append(nums2.pop(0))
            length2 -= 1
        elif length2 == 0:
            nums.append(nums1.pop(0))
            length1 -= 1
        elif nums1[0] <= nums2[0]:
            nums.append(nums1.pop(0))
            length1 -= 1
        elif nums1[0] > nums2[0]:
            nums.append(nums2.pop(0))
            length2 -= 1
        else:
            break
    middle = int(times / 2)
    if times % 2 == 0:
        return (nums[middle-1] + nums[middle]) / 2
    else:     
        return nums[middle]
def method2(nums1, nums2):
      m = len(nums1)
      n = len(nums2)
      start = 0
      end = 0
      middle = 0
      if nums1[0] < nums2[0]:
          nums1.pop(0)
# @lc code=end

