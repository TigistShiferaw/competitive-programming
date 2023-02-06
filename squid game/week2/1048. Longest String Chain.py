class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dic = {}
        word_set = set(words)
        
        for word in words:
            
            for i in range(97, 97 + 26):
                
                for j in range(len(word) + 1):
                    x = word[:j] + chr(i) + word[j:]
                    # print(word,x)
                    if x in word_set:
                        if word in dic:
                            dic[word].append(x)
                        else:
                            dic[word] = [x]
        dp = {}   
        def dfs(word):
            if word in dp:
                return dp[word]
            if word not in dic:
                return 1
            count = 0
            for d in dic[word]:
                count = max(count,dfs(d) + 1)
            dp[word] =  count
            return dp[word]
        ans = 0
        for w in words:
            ans = max(ans, dfs(w))
        return ans
            