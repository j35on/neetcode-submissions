class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max1 = 0
        curlength = 0
        
        for i in numset:
            if i-1 not in numset:
                curlength = 1
                current = i
                while current+1 in numset:
                    curlength += 1
                    current += 1
            max1 = max(max1,curlength)
        return max1