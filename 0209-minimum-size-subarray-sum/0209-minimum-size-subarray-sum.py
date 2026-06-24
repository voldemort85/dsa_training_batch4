class Solution:
    def minSubArrayLen(self, target, nums):
        low = 0
        curr_sum = nums[0]
        high=0
        min_len= float('inf')

        
        
        while high < len(nums):
            if target > curr_sum:
                high+=1
                if high < len(nums):
                    curr_sum+= nums[high]

            else:
                min_len=min(min_len,high-low+1)
                curr_sum-=nums[low]
                low+=1
            
         
        return 0 if min_len==float("inf") else min_len
                

        

