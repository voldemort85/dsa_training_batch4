class Solution(object):
    def subarraySum(self, nums, k):
        d={0:1}
        count=0
        current_sum=0
        for num in nums:
            current_sum=current_sum+num

            if current_sum-k in d:
                count=count+d[current_sum-k]

            d[current_sum]=d.get(current_sum,0)+1
        return count       
