class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c=0
        citations.sort()
        for i in range(len(citations)):
            if citations[i]>=len(citations)-i:
                c=i+1
                break
        if c==0:
            return 0
        else:
            return len(citations)-(c-1)