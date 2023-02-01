class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        data = []

        for i in range(len(scores)):
            data.append((ages[i],scores[i]))
            data.sort()

        dp = [0] * len(scores)

        for i in range(len(scores)):
            currScore = data[i][1]
            dp[i] = currScore
            for j in range(i):
                if data[j][1] <= currScore:
                    dp[i] = max(dp[i], dp[j] + currScore)
        return max(dp)
        


