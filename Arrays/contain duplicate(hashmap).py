class Solution(object):
    def containsDuplicate(self, nums):
        num=0
        seen={}
        for num in nums:
            if num in seen:
                return True
            seen[num]=True

        return False
        
