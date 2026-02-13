class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        max_area=0

        while i<j :
            
         min_height=min(height[i],height[j])
        
         width=j-i

         max_area=max(width*min_height,max_area)

         if height[i]<=height[j]:
             i=i+1
         else:
             j=j-1
        return max_area
           

