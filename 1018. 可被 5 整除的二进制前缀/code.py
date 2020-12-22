class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        ans = int(A[0])
        if ans==0:
            A[0]=1
        else:
            A[0]=0
        for i in range(1,len(A)):
            if A[i]==0:
                ans = ans*2
            if A[i]==1:
                ans = ans*2+1
            A[i] = (ans%5==0)

        return A
