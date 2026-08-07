class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxleft = height[left]
        maxright=height[right]
        totalWater = 0

        while left < right:
            if maxleft < maxright or maxleft == maxright:
                if min(maxleft, maxright) - height[left] > 0:
                    totalWater += min(maxleft, maxright) - height[left]
                left += 1
                maxleft=max(maxleft, height[left])
            else:
                if min(maxleft, maxright) - height[right] > 0:
                    totalWater += min(maxleft, maxright) - height[right]
                right -= 1
                maxright=max(maxright, height[right])
        return totalWater
                
        