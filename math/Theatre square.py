import math
def TheaterSquare():
        neededFlagstones=0
        n,m,a=list(map(int,(input().rstrip().split())))
        print(math.ceil(n/a)*math.ceil(m/a))
TheaterSquare()