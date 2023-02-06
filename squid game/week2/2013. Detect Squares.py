class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1
        
    def count(self, point: List[int]) -> int:
        ans = 0
        pt1x = point[0]
        pt1y = point[1]
        for pt in self.points:
            if pt != point:
                xdiff = abs(pt1x - pt[0])
                ydiff = abs(pt1y - pt[1])
                if xdiff == 0 and ydiff > 0:
                    tmpdiffX = ydiff
                    if (pt1x - tmpdiffX,pt[1]) in self.points and (pt1x - tmpdiffX,pt1y) in self.points:
                        ans += (self.points[(pt1x - tmpdiffX,pt[1])] * self.points[(pt[0],pt[1])] * self.points[(pt1x - tmpdiffX,pt1y)])
                    if (pt1x + tmpdiffX,pt[1]) in self.points and (pt1x + tmpdiffX,pt1y) in self.points:
                        ans += (self.points[(pt1x + tmpdiffX,pt[1])] * self.points[(pt[0],pt[1])] * self.points[(pt1x + tmpdiffX,pt1y)])
            # print(self.points)
            if (pt1x, pt1y) in self.points and (self.points[(pt1x, pt1y)])  == 0:
                del(self.points[(pt1x, pt1y)])               
        return ans