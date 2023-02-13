class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        def dec(x):
            tot = 0
            for i in range(len(x) - 1,-1,-1):
                n = len(x) - 1
                tot += int(x[i]) *  pow(2, (n - i))
            return tot
        c = dec(a)
        d = dec(b)
        x = bin(int(c)+int(d))
        x = x[2:]
        for i in range(2,len(x)):
            if  dec(x) == c + d:
                return x
            x = x[1:]
        return x
        