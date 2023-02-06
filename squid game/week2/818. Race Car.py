class Solution:
    def racecar(self, target: int) -> int:


        queue = deque()
        queue.append((0,1,0))
        vis = set()
        while queue:
            
            pos, speed, cnt = queue.popleft()
            if pos == target:
                return cnt
            if (pos,speed) not in vis:
                vis.add((pos, speed))
                if speed < 0:
                    queue.append((pos, 1, cnt + 1))
                else:
                    queue.append((pos, -1, cnt + 1))
        
                queue.append((pos + speed, speed * 2, cnt + 1))



        # memo = {}

        # def rec(target, currPos, speed,ans):
        #     if currPos < - 10 ** 4 or currPos > 10 ** 4:
        #         return inf
        #     # if 
        #     if currPos == target:
        #         return 0
        #     if (currPos,speed) in memo:
        #         return memo[(currPos,speed)]
        #     if speed < 0:
        #         rev = rec(target, currPos, 1) + 1
        #     else:
        #         rev = rec(target, currPos, -1) + 1
        #     acc = rec(target, currPos + speed, speed * 2) + 1
        #     memo[(currPos, speed)] = min(acc, rev)
        #     return memo[currPos, speed]
        # return rec(target, 0, 1)