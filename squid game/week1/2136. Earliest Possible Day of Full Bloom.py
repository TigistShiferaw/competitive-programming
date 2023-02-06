class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plantGrowMap = []
        for i in range(len(plantTime)):
            plantGrowMap.append((growTime[i], plantTime[i]))

        plantGrowMap.sort(reverse = True)

        currentTime = 0
        ans = 0

        for i in range(len(plantGrowMap)):
            currentTime += plantGrowMap[i][1]
            ans = max(ans, currentTime + plantGrowMap[i][0])
        return ans