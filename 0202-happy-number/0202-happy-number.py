class Solution(object):
    def isHappy(self, n):
        
        def square(n):
            sum=0
            while n>0:
                digit=n%10
                sum=sum+digit*digit
                n=n//10
                
            
            return sum 

        
        slow = n 
        fast = n 
        while fast!=1:

            slow=square(slow)
            fast=square(square(fast))
            

            if slow==fast and slow!=1 :
                return False
    
        return True