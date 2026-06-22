class Solution(object):
    def maxArea(self, height):
        n=len(height)
        left=0
        right=n-1
        max_area=0
        

        while left<right:

            

            width=right-left
            length=min(height[left],height[right])

            area=width*length

            if height[left]< height[right]:
                left+=1

            else:
                right-=1
                

            if max_area < area:
                max_area=area
        
        return max_area
