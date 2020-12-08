class Solution(object):
    def isSubsequence(self, s, t):
        m = len(s)
        n = len(t)
        sign = -1
        for i in range(m):
            for j in range(sign+1,n):
                if t[j] == s[i]:
                    sign = j
                    break
            else:
                return False
        return True
        
            
