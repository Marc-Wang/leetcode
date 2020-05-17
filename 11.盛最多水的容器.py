#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max area means width * Height = Max
        i = 0
        j = len(height)-1
        maxArea = 0
        area = 0
        while i < j:
            if height[i] < height[j]:
                area = height[i]*(j-i)
                # maxArea = max(maxArea, height[i]*(j-i))
                i += 1
            else:
                area = height[j]*(j-i)
                # maxArea = max(maxArea, height[j]*(j-i))
                j -= 1
            if area > maxArea:
                maxArea = area
        return maxArea

# @lc code=end

