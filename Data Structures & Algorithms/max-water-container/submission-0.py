class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        res = 0

        while left < right:
            if(right-left) * min(heights[left],heights[right]) > res:
                res = (right-left) * min(heights[left],heights[right])
            elif heights[right] < heights[left]:
                right-=1
            else:
                left+=1
        return res


        