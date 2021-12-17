import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nearest=[]
        distance=[]
        for i in range(len(points)):
            dist=math.sqrt((((points[i])[0])**2)+((points[i][1])**2))
            distance.append((dist,points[i]))
        distance.sort()
        
        for i in range(k):
            nearest.append(distance[i][1])
            
            
        return nearest