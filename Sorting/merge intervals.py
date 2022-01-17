class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr=[]
        i=0
        
        while i<len(intervals):
            first=intervals[i][0]
            last=intervals[i][1]
            i+=1
            while i<len(intervals) and last>=intervals[i][0]:
                if last<intervals[i][1]:
                    last=intervals[i][1]
                i+=1
                
            arr.append((first,last))    
        return  arr                  