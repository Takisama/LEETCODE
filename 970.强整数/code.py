class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        answer = set()
        for i in range(20):
            for j in range(20):
                v=x**i + y**j
                if v<=bound:
                    answer.add(v)
        return list(answer)
