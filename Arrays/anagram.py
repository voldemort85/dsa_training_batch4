class Solution(object):
    def isAnagram(self, s, t):
        count={}
        s=s.lower()
        t=t.lower()
        if len(s)!=len(t):
            return False
        else:
            for ch in s:
                count[ch]=count.get(ch,0)+1
            for ch in t:
                if ch not in count:
                    return False
                count[ch]=count[ch]-1
                if count[ch]==0:
                    del count[ch]
            if len(count)==0:
                return True
            else :
                return False

