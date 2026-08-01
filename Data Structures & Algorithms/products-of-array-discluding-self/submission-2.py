class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result =[0] * len(nums)
        zeroes = 0
        allmulti = 1
        for i in nums:
            if(i == 0):
                zeroes += 1
            
            else:
                allmulti = allmulti * i
        
        for i in range(len(nums)):
            if(zeroes >= 2):
                result[i] = 0
            elif(zeroes == 1):
                if(nums[i] == 0):
                    result[i] = allmulti
                else:
                    result[i] = 0
            else:
                if(nums[i] == 0):
                    result[i] = 0
                else:
                    result[i] = allmulti // nums[i]
        return result

        



        